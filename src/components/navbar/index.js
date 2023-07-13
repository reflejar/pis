import React, { useState } from "react"

import { PopupButton } from '@typeform/embed-react'
import "./styles.scss"


const Navbar = () => {
    const [isActive, setIsActive] = useState(false);

    return (
        <nav id="navbar" className={(isActive ? 'navbar is-active' : 'navbar')} role="navigation" aria-label="main navigation">
            <div className="navbar-brand ">
                <button onClick={() => setIsActive(prevState => !prevState)} className={(isActive ? 'navbar-burger is-active' : 'navbar-burger')} aria-label="menu" aria-expanded="false" data-target="navbarColapse">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </button>
            </div>

            <div id="navbarColapse" className={(isActive ? 'navbar-menu is-active' : 'navbar-menu')}>
                <div className="navbar-start">
                    <div className="left-wrapper">
                        <a className="navbar-item" onClick={() => setIsActive(false)} href="/">
                            PIS
                        </a>                  
                    </div>


                    <a className="navbar-item" href="/#herramientas" rel="noopener noreferrer">
                        Herramientas
                    </a>   

                    <a className="navbar-item" href="/#testeos" rel="noopener noreferrer">
                        Testeos
                    </a>                      
                    <a className="navbar-item" href="/#faqs" rel="noopener noreferrer">
                        FAQs
                    </a>                                           
                    <a className="navbar-item" href="/#nosotros" rel="noopener noreferrer">
                            Nosotros
                    </a>   
                    <PopupButton id="bkXtFW" className="navbar-item donate" rel="noopener noreferrer">
                        Donar
                    </PopupButton>


                    <a className="navbar-item is-hidden-desktop" href="mailto:contacto@democraciaenred.org">
                        contacto@democraciaenred.org
                    </a>
                    <a className="navbar-item is-hidden-desktop is-inline-block" href="https://www.facebook.com/democraciaenred/" target="_blank" rel="noopener noreferrer">
                        <span className="icon">
                            <i className="fas fab fa-facebook-square"></i>
                        </span>
                    </a>
                    <a className="navbar-item is-hidden-desktop is-inline-block" href="https://twitter.com/fundacionDER" target="_blank" rel="noopener noreferrer">
                        <span className="icon">
                            <i className="fas fab fa-twitter"></i>
                        </span>
                    </a>
                    <a className="navbar-item is-hidden-desktop is-inline-block" href="https://www.instagram.com/democraciaenred/" target="_blank" rel="noopener noreferrer">
                        <span className="icon">
                            <i className="fas fab fa-instagram"></i>
                        </span>
                    </a>
                    <a className="navbar-item is-hidden-desktop is-inline-block" href="https://github.com/democraciaenred" target="_blank" rel="noopener noreferrer">
                        <span className="icon">
                            <i className="fas fab fa-github"></i>
                        </span>
                    </a>
                    <p className="is-size-7 is-hidden-desktop has-text-white">Desarrollado por <a className="has-text-underline has-text-white" href="https://democraciaenred.org/" target="_blank" rel="noopener noreferrer">Democracia en Red</a></p>
                </div>
            </div>
        </nav>
    )
};

export default Navbar;