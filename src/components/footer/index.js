import React from "react"
import "./styles.scss"

import { PopupButton } from '@typeform/embed-react'
import logo_der from "./assets/logo-der-white.svg"

export default () =>  {

    return (
        <section className="footer section has-background-grey-dark	has-text-white">
            <div className="container">

            <div className="columns is-vcentered">
                <div className="column is-3">
                    <a href="https://democraciaenred.org" target="_blank"><img src={logo_der} className="image mb-3" width="180"/></a>
                    <p className="is-size-7">footer.description</p>
                </div>
                    <div className="column is-offset-1 is-4">
                        <h4 className="title is-4 is-spaced">footer.title</h4>
                        <p className="is-size-7">
                            footer.copyright_1 <a className="has-text-underline" href="https://democraciaenred.org/" target="_blank" rel="noopener noreferrer">Democracia en Red</a>footer.copyright_2
                        </p>
                    </div>
                <div className="column is-offset-1 is-3">
                    <ul>
                            <li><a className="footer-link" href="https://democraciaos.org/es/#productos">products_title</a></li>
                            <li><a className="footer-link" href="https://democraciaos.org/es/#nosotros">us.title</a></li>
                            <li>
                            <PopupButton id="bkXtFW" className="button is-rounded is-medium is-dark" rel="noopener noreferrer">donate</PopupButton>
                            </li>
                            <li className="footer-link has-text-underline"><a href="mailto:	contacto@democraciaenred.org">contacto@democraciaenred.org</a></li>
                            <li>
                                <a href="https://www.facebook.com/democraciaenred/" target="_blank" rel="noopener noreferrer">
                                    <span className="icon">
                                        <i className="fas fab fa-facebook-square"></i>
                                    </span>
                                </a>
                                <a href="https://twitter.com/fundacionDER" target="_blank" rel="noopener noreferrer">
                                    <span className="icon">
                                        <i className="fas fab fa-twitter"></i>
                                    </span>
                                </a>
                                <a href="https://www.instagram.com/democraciaenred/" target="_blank" rel="noopener noreferrer">
                                    <span className="icon">
                                        <i className="fas fab fa-instagram"></i>
                                    </span>
                                </a>
                                <a href="https://github.com/democraciaenred" target="_blank" rel="noopener noreferrer">
                                    <span className="icon">
                                        <i className="fas fab fa-github"></i>
                                    </span>
                                </a>
                            </li>
                    </ul>
                    </div>
            </div>   
            </div>
        </section>
    )
}