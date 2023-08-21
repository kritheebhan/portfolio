import React, { useRef } from 'react';
import emailjs from '@emailjs/browser';
import contactimg from '../components/images/contact.png'
import insta from '../components/images/instagram.svg'
import link from '../components/images/linkedin-in.svg'
import twitter from '../components/images/twitter.svg'
import message from '../components/images/message.svg'
import cloud from '../components/images/cloud.svg'

function Contacts() {
    const form = useRef()

    const sendEmail = (e) => {
      e.preventDefault();
  
      emailjs.sendForm('service_3aqq8rs', 'template_ysoak4j', form.current, 'eOa4Oeau6VIqKL4nc')
        .then((result) => {
            console.log(result.text);
            document.getElementById( 'after-submit' ).style.display = 'block';
            document.getElementById( 'before-submit' ).style.display = 'none';

        }, (error) => {
            console.log(error.text);
            document.getElementById ( 'not-submit' ).style.display = 'block';
            document.getElementById( 'before-submit' ).style.display = 'none';

        });
        e.target.reset()
    };
  
  return (
    <div className='section-4' id='contact'>
      <div className='split '>
        <div className='contant'>
         <div className='card-contact mt-10'>
            <div className='flex justify-center mb-6'>
              <img src={contactimg} alt="" className='h-12' />
            </div>
            <h2 className="text-3xl lg:text-5xl font-semibold text-center ">Got a project in mind? <br /> Let's get in touch.</h2>
            <form ref={form} onSubmit={sendEmail} id='before-submit'>
              <div className=' grid  md:grid-cols-2 place-items-center mt-6 md:mt-16'>
                <input type="text" id="first_name" placeholder="What is your name * " className='text-box' name='user_name' required />
                <input type="text" id="first_name" placeholder="Your email address * " className='text-box' name='user_email'required/>
                <textarea name="message" id="" cols="5" rows="5" placeholder="Tell me about your project *"  className='text-area md:col-span-2 mt-10 md:mt-14 'required></textarea>
                <button type="submit" value="submit" className='submit-btn border-2 border-slate-900 rounded-lg font-bold md:col-span-2 ' onclick="message" >Submit</button>
              </div>
            </form>
            <div className='submit ' id='after-submit'>
              <h2 >Thank you! Your submission has been receives!</h2>
            </div>
            <div className='submit ' id='not-submit'>
              <h2 >Oops! Something went wrong while submitting the form.</h2>
            </div>
         </div>
        </div>
        <div className='footer md:flex justify-center'>
          <h2 className='text-3xl lg:text-4xl'>Kritheebhan</h2>
             <a href="https://instagram.com/kritheebhan?utm_source=qr&igshid=ZDc4ODBmNjlmNQ%3D%3D" target="_blank" className='social-media'><img src={insta} alt="" /></a>
             <a href="https://www.linkedin.com/in/kritheebhan-b-8b130b213" target="_blank" className='social-media'><img src={link} alt="" /></a>
             <a href="" className='social-media'><img src={twitter} alt="" /></a>
        </div>
      </div> 
    </div>
  )
}

export default Contacts