import {useEffect, useState} from "react";

export const Orders = () => {
    const [product_id, setId] = useState('');
    const [quantity, setQuantity] = useState('');
    const [message, setMessage] = useState('Buy your favorite product');

    useEffect(() => {
        (async () => {
            try {
                if (product_id) {
                    const response = await fetch(`http://localhost:8000/products/${product_id}`);
                    const content = await response.json();
                    const price = parseFloat(content.price) * 1.2;
                    setMessage(`Your product price is $${price}`);
                }
            } catch (e) {
                setMessage('Buy your favorite product');
            }
        })();
    }, [product_id]);

    const submit = async e => {
        e.preventDefault();

        const url = new URL('http://localhost:8001/orders');
        url.searchParams.append('product_id', product_id);
        url.searchParams.append('quantity', quantity);

        if (quantity <= 0) {
            setMessage('Invalid data');
            document.getElementById('message').classList.add('error-message');
            return;
        }

        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });

        const content = await response.json();
        const total_price = parseFloat(content.total) * parseInt(content.quantity);

        if (response.status === 400) {
            setMessage('Insufficient quantity available');
            document.getElementById('message').classList.add('error-message');
            return;
        } else if (response.status === 404) {
            setMessage('The product is not found');
            document.getElementById('message').classList.add('error-message');
            return;
        } else if (response.status === 422) {
            setMessage('All fields are required');
            document.getElementById('message').classList.add('error-message');
            return;
        }

        document.getElementById('message').classList.remove('error-message');
        setMessage(`Thank you for your order! You spent $${total_price}`);
    }

    return <div className="container">
        <main>
            <div className="py-5 text-center">
                <h2>Checkout form</h2>
                <p id="message" className="lead">{message}</p>
            </div>

            <form onSubmit={submit}>
                <div className="row g-3">
                    <div className="col-sm-6">
                        <label className="form-label">Product's id</label>
                        <input className="form-control"
                               onChange={e => setId(e.target.value)}
                        />
                    </div>

                    <div className="col-sm-6">
                        <label className="form-label">Quantity</label>
                        <input type="number" className="form-control"
                               onChange={e => setQuantity(e.target.value)}
                        />
                    </div>
                </div>
                <hr className="my-4"/>
                <button className="w-100 btn btn-primary btn-lg" type="submit">Buy</button>
            </form>
        </main>
    </div>
}