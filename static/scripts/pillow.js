

/*simple example of selecting h1 html header file and adding text context
const myHeading = document.querySelector('h1');
myHeading.textContent = 'HELLO!';
*/

/*Event Example
-select html element
-addEventListener = sets up a function that will be called (function) that will be called
whenever specified event (click) is delivered to target
-functions that are passed to addEventListener are called anonymous functions (in this example, function())
    -can also replace function() with arrow funtion '() =>'

document.querySelector('html').addEventListener('click',function(){
    alert("Hi")
})

*/

//let x --> declares a value x

/*
can combine different types in an array and access it as a normal array

let array = [1,'Bob','Steve',10];

*/ 

/* changing pictures when clicked
let myImage = document.querySelector('img');

myImage.onclick = function(){
    let mySrc = myImage.getAttribute('src');
    if (mySrc === 'images/pillow.jpg'){
        myImage.setAttribute( 'src', 'images/noodle.jpg');
    }
    else{
        myImage.setAttribute( 'src', 'images/pillow.jpg');
    }
}
*/

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');


function setUserName(){
    let myName = prompt('Please enter your name'); //contains a prompt(displays a dialog box) 
    localStorage.setItem('name', myName); //stores name in local storage
    myHeading.textContent = 'Logged in as user: ' + myName;
}

if (!localStorage.getItem('name')){ //checks if stored in localStorage and if it isn't, call function to create it
    setUserName();
}
else {
    let storedName = localStorage.getItem('name');
    myHeading.textContent = 'Logged in as user: ' + myName;
}

myButton.onclick = function () {setUserName();}