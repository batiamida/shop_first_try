//elements
const itemImg = document.querySelectorAll('.pitems__item h2');
const itemUl = document.querySelectorAll('.pitems__item ul');
const brends = document.querySelector('.sidebar__brends_list');
const price = document.querySelector('.sidebar__price_flex');
const sidebarI = document.querySelector('.sidebar i'); 

//buttons
const itemColor = document.querySelectorAll('.pitems__item_color');
const buttonForHide = document.querySelectorAll('.sidebar__open')

//for identical height of header on image
let itemImgBiggest = 0;
itemImg.forEach(img => {
	if (img.offsetHeight >= itemImgBiggest) {
		itemImgBiggest = img.offsetHeight;
	}
})

itemImg.forEach(img => {
	img.style.height = `${itemImgBiggest}px`;	
})

//if click to know a colors of element
itemColor.forEach(color => {
	color.addEventListener('click', function() {
		if (this.nextElementSibling.style.display === 'block') {
			this.nextElementSibling.style.display = '';
		} else {
			this.nextElementSibling.style.display = 'block';
		}
	})
})

//if click button in sidebar
buttonForHide.forEach(button => {
	button.addEventListener('click', function() {
		if (this.nextElementSibling.style.display === 'none') {
			this.nextElementSibling.style.display = '';
			this.parentElement.querySelector('i').style.transform = ''
			this.parentElement.querySelector('i').style.padding = ''
			this.parentElement.querySelector('i').style.margin = ''
		}  else {
			this.nextElementSibling.style.display = 'none';
			this.parentElement.querySelector('i').style.transform = 'rotate(45deg)'
			this.parentElement.querySelector('i').style.padding = '11px'
			this.parentElement.querySelector('i').style.margin = '0px 0 0px 0'
		}
	})
})