import React, { Component, useState } from 'react'
import { Link } from 'react-scroll'
import "./Navebar.css"
import insta from "../images/instagram.svg"
import link from "../images/linkedin-in.svg"
import twitter from "../images/twitter.svg"

export default class Navebar extends Component {
  state ={clicked: false};
  handleClick = () =>{
  this.setState({clicked: !this.state.clicked})
  }
  render() { 
    return (
      <div>
        <nav className='containe nav' >
            <a href="Home.jsx" className='text-3xl lg:text-4xl'>Kritheebhan</a>

        <div className='active'>
            <ul id="navbar" className={this.state.clicked ? "#navbar active" : "#navbar"}>
                <li><Link to="intro" spy={true} smooth={true} offset={-100} duration={900} style={{ cursor: 'pointer' }} >Home</Link></li>
                <li><Link to="Works" spy={true} smooth={true} offset={-100} duration={900} style={{ cursor: 'pointer' }} >Works</Link></li>
                <li><Link to="about" spy={true} smooth={true} offset={-100} duration={900} style={{ cursor: 'pointer' }} >About</Link></li>
                <li><Link to="contact" spy={true} smooth={true} offset={50} duration={900} style={{ cursor: 'pointer' }} >Contact</Link></li>
            </ul>
        </div>
        <div className='mobail' onClick={this.handleClick}>
          <i id="bar" className={this.state.clicked ? "fas fa-times" : "fas fa-bars"}></i>
        </div>
        <div className="navimg hidden lg:flex">
             <a href="https://instagram.com/kritheebhan?utm_source=qr&igshid=ZDc4ODBmNjlmNQ%3D%3D" target="_blank" className='media'><img src={insta} alt="" /></a>
             <a href="https://www.linkedin.com/in/kritheebhan-b-8b130b213" target="_blank" className='media'><img src={link} alt="" /></a>
             <a href="" className='media'><img src={twitter} alt="" /></a>
        </div>
        </nav>
      </div>
    )
  }
}
