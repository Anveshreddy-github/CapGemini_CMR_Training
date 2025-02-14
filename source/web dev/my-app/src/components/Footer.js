import React from "react";

function Footer(){
    return(
        <footer style={styles.Footer}>
            <p>&copy; 2024 My Website. All rights reserved. </p>
        </footer>
    );
}

const styles = {
    Footer:{
        background :"#333",
        color:"white",
        textAlign:"center",
        padding:"10px",
        position:"fixed",
        width:"100%",
        bottom:0
    }
}
export default Footer;