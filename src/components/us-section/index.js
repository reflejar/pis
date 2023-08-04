import React from "react"
import "./styles.scss"
import image from "./assets/slider1.jpg"

export default ({ data }) =>  {

    return (
        <section id="nosotros" className="hero is-fullheight is-large is-dark us-section" style={{ backgroundImage:`url("${image}")`}}>
            <div className="hero-body">
                <div className="container has-text-centered">
                    <h3 className="title is-spaced is-size-1-desktop">
                        ¿QUIÉNES SOMOS?

                    </h3>
                    <p className="subtitle is-size-4-desktop">
                        Somos Democracia en Red, una organización radicada en Argentina. Conformada por personas activistas, programadores y científicos sociales, que desde el hacer buscamos abrir las instituciones públicas y los procesos de toma de decisión.
                    </p>
                    <a className="has-text-urine has-text-underline is-size-5" href="https://democraciaenred.org" target="_blank" rel="noopener noreferrer"> democraciaenred.org</a>
                </div>
            </div>
        </section>
    )
}