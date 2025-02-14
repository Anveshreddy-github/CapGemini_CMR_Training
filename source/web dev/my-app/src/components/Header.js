import React from "react";
function Header(){
    return(
        <header style={Styles.header}>
            <h1>Erripuk JP</h1>
            <nav>
                <ul style={Styles.navList}>
                    <li><a href="#" style={{ color: 'white', textDecoration: 'none', padding: '0 10px' }} onMouseOver={(e) => e.target.style.color = 'orange'} onMouseOut={(e) => e.target.style.color = 'white'}>Home</a></li>
                    <li><a href="#" style={{ color: 'white', textDecoration: 'none', padding: '0 10px' }} onMouseOver={(e) => e.target.style.color = 'blue'} onMouseOut={(e) => e.target.style.color = 'white'}>About</a></li>
                    <li><a href="#" style={{ color: 'white', textDecoration: 'none', padding: '0 10px' }} onMouseOver={(e) => e.target.style.color = 'green'} onMouseOut={(e) => e.target.style.color = 'white'}>Contact</a></li>
                </ul>
            </nav>
        </header>
    );
}

const Styles = {
    header: {
        background: '#333',
        color: 'white',
        padding : '10px',
        textAlign: 'center',
    },
    navList: {
        listStyleType: 'none',
        padding: '0',
        display: 'flex',
        justifyContent: 'center',
    }
}
export default Header;