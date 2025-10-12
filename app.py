body {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    text-align: center;
    background-color: #ffd8e2;
    padding: 20px;
}

h1 {
    font-family: monaco, monospace;
    color:#d61142;
    margin-bottom: 5px;
}

textarea, input[type=text] {
    margin-top: 7px;
    width: 75%;
    padding: 5px;
}

button {
    margin-top: 10px;
    background-color: #ec266f;  
    color: white;              
    padding: 10px 20px;         
    text-decoration: none;      
    border-radius: 5px; 
    border-width: 2px;  
    border-color: #d91942;     
    font-family: Andale Mono, monospace;
    font-weight: lighter;
    transition: 0.3s;
}

button:hover {
    background-color: #db2553;
}

.build {
    margin-bottom: 2px;
}

p2 {
    color: #db173b;
    font-family: Andale Mono, monospace;
    font-size: smaller;
}

#chat-container {
    width: 75%;
    margin-top: 20px;
}

#chat-box {
    border: 2px solid #db173b;
    height: 300px;
    overflow-y: scroll;
    padding: 10px;
    background-color: #fff0f5;
    margin-bottom: 5px;
}

#user-input {
    width: 80%;
    padding: 5px;
}

#send-btn {
    width: 18%;
}
