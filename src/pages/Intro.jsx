import React from 'react'
import { Link } from 'react-scroll'
import "../App.css"
import "./pages.css"
import hello from '../components/images/hello.png'
import under_line from '../components/images/under_line.svg'
import mypic from '../components/images/imgabout.png'

const Home = () => {
  return (
    <div className='containe ' id="intro">
      <div className='text-center lg:text-left lg:py-64 py-48 ' id='intro-1'>
        <div className='flex justify-center lg:justify-start'>
        <img src={hello} alt="" className='h-14 mb-6 '/>
        </div>
        <h2 className='text-4xl lg:text-7xl md:text-6xl font-semibold'>
          I'm Kritheebhan,<br/>a Full stack developer.
          </h2>
          <img src={under_line} alt="" className='ml-10 w-40 lg:w-auto lg:ml-20 ' />
          <Link to="Works" spy={true} smooth={true} offset={-100} duration={900} style={{ cursor: 'pointer' }} ><button className="btn border-2 border-slate-900 rounded-lg font-bold">See My Works</button></Link>
        
      </div>
      <div className='pt-36 flex justify-center'  id='intro-2'>
      {/* <img src={mypic} alt="" className='aboutimg ' /> */}
      </div>
    </div>
  )
}

export default Home