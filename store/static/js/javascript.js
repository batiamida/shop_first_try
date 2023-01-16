//elements
const favoritesImages = document.querySelectorAll('.favorites__images');
const favoritesImg = document.querySelectorAll('.favorites__image_img');
const favoritesImg_1 = document.querySelector('.favorites__images_1');
const favoritesImg_2 = document.querySelector('.favorites__images_2');
const favoritesImg_3 = document.querySelector('.favorites__images_3');
const favoritesInline = document.querySelector('.favorites__select_inline');

//buttons
const shoes = document.querySelector('#shoes');
const apparel = document.querySelector('#apparel');
const basics = document.querySelector('#basics');
const imageButtons = document.querySelectorAll('.favorites__image_img button');

//click on buttons for change images
shoes.addEventListener('click', function() {
	favoritesImages.forEach(img => {
		img.style.display = 'none';
	})
	favoritesImg_1.style.display = 'flex';
	favoritesInline.style.left = '37.7%';
})
apparel.addEventListener('click', function() {
	favoritesImages.forEach(img => {
		img.style.display = 'none';
	})
	favoritesImg_2.style.display = 'flex';
	favoritesInline.style.left = '46.7%';
})
basics.addEventListener('click', function() {
	favoritesImages.forEach(img => {
		img.style.display = 'none';
	})
	favoritesImg_3.style.display = 'flex';
	favoritesInline.style.left = '56%';
})

//hover on images for appear button
favoritesImg.forEach(img => {
	img.addEventListener('mouseover', function() {
		this.querySelector('button').style.opacity = '1';
	})
	img.addEventListener('mouseout', function() {
		this.querySelector('button').style.opacity = '';
	})
})