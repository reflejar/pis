import React from "react"
import "./styles.scss"

import amartya from "./assets/amartya.png"
import art41 from "./assets/art_41.png"
import reflejar from "./assets/reflejar.png"
import coplasa from "./assets/coplasa.png"
import naturaleza from "./assets/naturaleza.png"
import simbiosis from "./assets/simbiosis.png"
import quinta_esencia from "./assets/quinta_esencia.png"
import lab from "./assets/lab.png"

export default () =>  {

    return (
        <section id="work-with" className="section work-with">
            <div className="container has-text-centered">
                <h3 className="main-title title is-4 is-size-1-desktop has-text-black">
                    Trabajamos con:
                </h3>
                <div className="columns is-multiline">
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={amartya} className="client-logo" alt=""/>
                        </figure>
                    </div>
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={art41} className="client-logo" alt=""/>
                        </figure>
                    </div>
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={reflejar} className="client-logo" alt=""/>
                        </figure>
                    </div>
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={coplasa} className="client-logo" alt=""/>
                        </figure>
                    </div>
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={naturaleza} className="client-logo" alt=""/>
                        </figure>
                    </div>
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={simbiosis} className="client-logo" alt=""/>
                        </figure>
                    </div>
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={quinta_esencia} className="client-logo" alt=""/>
                        </figure>
                    </div>
                    <div className="column is-one-quarter-tablet is-one-quarter-desktop is-half-mobile">
                        <figure className="image">
                            <img src={lab} className="client-logo" alt=""/>
                        </figure>
                    </div>
                </div>
            </div>
        </section>
    )
}