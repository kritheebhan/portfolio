import React from 'react'
import "../App.css"
import work from '../components/images/works.png'
import scribble from "../components/images/scribble.svg"
import shine_pink from '../components/images/shine pink.svg'
import machine_learning from '../components/images/machine-learning.png'
import crypto_graphy from '../components/images/crypto_graphy.png'
import portfolio from '../components/images/portfolio.svg'
import java from '../components/images/java.png'

function Work() {
  return (
    <div className='containe section-2 mt-14 lg:mt-0' id='Works'>
      <img src={scribble} alt="" className='heart h-18 hidden md:block'/>
      <img src={shine_pink} alt="" className='heart h-13  ml-auto hidden md:block'/>
      <div className='flex justify-center mt-10 lg:mt-0'>
        <img src={work} alt="" className='h-12'/>
      </div>
      <div className='text-center'>
      <p className='text-4xl lg:text-5xl font-semibold mt-6'>Check out some of my works</p>
      </div>

      <div className='card my-10'>
          <div className='border-2 border-slate-900 rounded-xl lg:flex p-10 m-4' id='ml'>
            <img src={machine_learning} alt="" id='icon' />
            <p className='paragraph-large lg:pl-10 mt-7 font-semibold'>Automatic skin cancer detection
            <p className='pargraph-small mt-2 '>Based on the feature extraction module of the proposed recognition model and U-Net architecture a lightweight CNN model.</p>
            </p>
          </div>

          <div className='border-2 border-slate-900 rounded-xl lg:flex p-10 m-4' id='cg'>
            <img src={crypto_graphy} alt="" id='icon' />
            <p className='paragraph-large lg:pl-10 mt-7  font-semibold'>Digital Certificate Authentication
            <p className='pargraph-small mt-2 '>Cryptography authentication method using digital signatures that are used as confidential evidence and validation of digital certificate ownership.</p>
            </p>
          </div>

          <div className='border-2 border-slate-900 rounded-xl lg:flex p-10 m-4' id='pt'>
            <img src={portfolio} alt="" id='icon'/>
            <p className='paragraph-large  lg:pl-10 mt-7  font-semibold'>Automatic skin cancer detection
            <p className='pargraph-small mt-2 '>A portfolio is a compilation of academic and professional materials. It provides insight into your personality and work ethic.</p>
            </p>
          </div>

          <div className='border-2 border-slate-900 rounded-xl lg:flex p-10 m-4' id='ja'>
            <img src={java} alt="" id='icon' />
            <p className='paragraph-large  lg:pl-10 mt-7  font-semibold'>E - Health Care System
            <p className='pargraph-small mt-2 '>E health care management system is a web-based application that assists in management of staff, Doctors and patients in easy.</p>
            </p>
          </div>
          
      </div>

     <div className='flex justify-center mb-20'>
        <a href="https://github.com/kritheebhan?tab=overview&from=2023-06-01&to=2023-06-30" target='blank'><button className="work-btn border-2 border-slate-900 rounded-lg font-bold ">More</button></a>
     </div>
     
    </div>
  )
}

export default Work