/* script.js */
document.addEventListener("DOMContentLoaded", () => {
    let tg = window.Telegram.WebApp;
    tg.expand(); // Развернуть WebApp на весь экран

    const orderButton = document.getElementById("order");
    const beerButton = document.getElementById("beer");
    const vodkaButton = document.getElementById("vodka");

    orderButton.addEventListener("click", () => {
        alert("Вы заказали напиток!");
    });

    beerButton.addEventListener("click", () => {
        alert("Вы выбрали Пиво!");
    });

    vodkaButton.addEventListener("click", () => {
        alert("Вы выбрали Водку!");
    });
});