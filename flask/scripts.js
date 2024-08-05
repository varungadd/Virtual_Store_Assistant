const products = {
    "apple iphone 13": { location: "sectionA", image: "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-13-finish-select-202207-pink_FMT_WHH?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1693063155178", sequence: 1 },
    "samsung galaxy s21": { location: "sectionB", image: "Samsung_s21.jpg", sequence: 2 },
    "lenovo yoga laptop": { location: "sectionC", image: "https://via.placeholder.com/100?text=Yoga+Laptop", sequence: 3 },
    "hp pavilion laptop": { location: "sectionD", image: "https://via.placeholder.com/100?text=Pavilion+Laptop", sequence: 4 },
    "nike running shoes": { location: "sectionE", image: "https://via.placeholder.com/100?text=Running+Shoes", sequence: 5 },
    "adidas sneakers": { location: "sectionF", image: "https://via.placeholder.com/100?text=Adidas+Sneakers", sequence: 6 },
    "sony wh-1000xm4 headphones": { location: "sectionG", image: "https://via.placeholder.com/100?text=WH-1000XM4", sequence: 7 },
    "amazon echo dot": { location: "sectionH", image: "images/amazon_echo_dot.jpg", sequence: 8 },
    "gopro hero9": { location: "sectionI", image: "https://via.placeholder.com/100?text=GoPro+Hero9", sequence: 9 },
    "puma sports jacket": { location: "sectionJ", image: "https://via.placeholder.com/100?text=Sports+Jacket", sequence: 10 }
    // Add more products as needed
};

function searchProduct() {
    const input = document.getElementById("product-input").value.toLowerCase();
    const productInfo = products[input];
    const productInfoDiv = document.getElementById("product-info");

    if (productInfo) {
        document.getElementById("product-image").src = productInfo.image;
        document.getElementById("product-location").innerText = `Located in ${productInfo.location.toUpperCase().replace('SECTION', 'Section ')}, Sequence ${productInfo.sequence}`;

        productInfoDiv.style.display = "block";
        highlightSection(productInfo.location);
    } else {
        alert("Product not found.");
        productInfoDiv.style.display = "none";
    }
}

function highlightSection(sectionId) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('highlight');
    });

    const section = document.getElementById(sectionId);
    if (section) {
        section.classList.add('highlight');
    }
}
