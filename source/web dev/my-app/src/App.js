import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Interest from "./components/Interest";
// Simple components
const Home = () => <h2>Home Page</h2>;
const About = () => <h2>About Page</h2>;

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>          

      <Routes>
        <Route path="/" element={<Interest />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;