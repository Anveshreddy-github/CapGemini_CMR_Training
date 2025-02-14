import React from "react";

function Body(){
    return (
        <main style={Styles.Main}>
            <h2>
                Welcome to my website
            </h2>
            <p>This is a simple React website with a structured layout</p>
        </main>
    );
}

const Styles ={
    Main: {
        padding:"20px",
        textAlign:"center"
    }
};
export default Body;