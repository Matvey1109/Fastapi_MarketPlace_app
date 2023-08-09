## Project's architecture

<div style="display: flex; margin: 0; justify-content: center; align-items: center; background-color: white;">
<img src="https://raw.github.com/Matvey1109/Fastapi_MarketPlace_app/main/screenshots/project%20architecture.png" alt="App Screenshot">
</div>

## Run Locally
```bash
uvicorn inventory.main:app --reload
uvicorn payment.main:app --reload --port=8001
npm start
```
## Screenshots

Products:
![App Screenshot](https://raw.github.com/Matvey1109/Fastapi_MarketPlace_app/main/screenshots/screenshot_products.png)

Order:
![App Screenshot](https://raw.github.com/Matvey1109/Fastapi_MarketPlace_app/main/screenshots/screenshot_order.png)