import React from 'react'
import "../App.css"
import About from "../components/images/About.png"
import Heart from "../components/images/heart.svg"
// import myimg from "../components/images/imgabout.png"


function about() {
  return (
    <div className='containe section-3' id='about' >
      <div className='flex justify-center img'>
         {/* <img src={myimg} alt="" className='aboutimg mt-5' />  */}
      </div>

      <div >
      <img src={Heart} alt="heart" className='h-20  ml-auto lg:mt-20 hidden md:block'/>
        <div className='flex justify-center lg:justify-start'>
        <img src={About} alt="" className='h-12 ' />
        </div>
        <div className='text-center sm:text-left'>
        <p className='text-4xl lg:text-5xl font-semibold mt-6'>More about me</p>
        <p className='paragraph-large mt-6 text-justify '>
        Hello! I’m Kritheebhan, a front-end developer and designer passionate about my work.
        </p>
        <p  className='pargraph-small mt-6 text-justify'>
        graduated in 2023 with a degree in Engineering and have a strong interest in web and app development. I’m seeking an entry-level position in software development with a respected organization where I can leverage my skills and continue learning.
        </p>
        <p className='pargraph-small mt-6 text-justify'>
        I am an enthusiastic and innovative learner eager to improve my skills and grow alongside the company.
        </p>
      </div>
      </div>
      <div className='cv my-6 lg:my-10'>
      <a href='Resume.pdf' download='Resume.pdf' className="about-btn border border-slate-900 rounded-lg font-bold">
        Downloade CV
        </a>
      </div>
    </div>
  )
}

export default about