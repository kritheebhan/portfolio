import React from "react";
import "./index.css";
import Navebar from "./components/Navbar/Navebar";
import Intro from "./pages/Intro";
import Works from "./pages/Works";
import About from "./pages/about";
import Contact from "./pages/Contacts"

function App() {

  return (
    <div>
      <Navebar/>
      <Intro/>
      <Works/>
      <About/>
      <Contact/>
    </div>
  );
}

export default App;
