function register(){

let user=document.getElementById("newUser").value;

let pass=document.getElementById("newPass").value;

localStorage.setItem(user,pass);

alert("Registration Successful");

window.location="index.html";

}

function login(){

let u=document.getElementById("user").value;

let p=document.getElementById("pass").value;

let storedPass=localStorage.getItem(u);

if(storedPass===p){

alert("Login Successful");

window.location="dashboard.html";

}

else{

alert("Invalid Login");

}

}

function logout(){

window.location="index.html";

}

let interviewQuestions = [

"What is pointer in C?",
"What is recursion?",
"What is stack?",
"What is queue?",
"What is linked list?",
"What is normalization in DBMS?",
"What is deadlock?",
"What is TCP/IP?",
"What is OSI model?",
"What is IP address?"

];

let codingQuestions = [

"Write a program to reverse a string",
"Write a program to find factorial",
"Write a program to check prime number",
"Write a program to print Fibonacci series",
"Write a program to check palindrome",
"Write a program to sort array",
"Write a program to find largest number",
"Write a program to swap two numbers",
"Write a program to count vowels",
"Write a program to print star pattern"

];

function showInterviewQuestion(){

let q = interviewQuestions[Math.floor(Math.random()*interviewQuestions.length)];

document.getElementById("question").innerText = q;

}

function showCodingQuestion(){

let q = codingQuestions[Math.floor(Math.random()*codingQuestions.length)];

document.getElementById("codingQuestion").innerText = q;

}

function runCode(){

let code = document.getElementById("code").value;

document.getElementById("output").innerText = code;

}


