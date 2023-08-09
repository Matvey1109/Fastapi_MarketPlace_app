import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Products} from "./components/Products";
import {ProductsCreate} from "./components/ProductsCreate";
import {Orders} from "./components/Orders";
import {Helmet} from 'react-helmet';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route
                    path="/"
                    element={
                        <>
                            <Helmet>
                                <title>Products</title>
                            </Helmet>
                            <Products/>
                        </>
                    }
                />
                <Route
                    path="/create"
                    element={
                        <>
                            <Helmet>
                                <title>Create product</title>
                            </Helmet>
                            <ProductsCreate/>
                        </>
                    }
                />
                <Route
                    path="/orders"
                    element={
                        <>
                            <Helmet>
                                <title>Order</title>
                            </Helmet>
                            <Orders/>
                        </>
                    }
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
