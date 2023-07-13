import React from "react"
import "./styles.scss"
import { PopupButton } from '@typeform/embed-react'

import pis_en_humanxs from "./assets/pis_en_humanxs.png"
import zonificacion_normativa from "./assets/zonificacion_normativa.png"
import agroquimicos_pba from "./assets/agroquimicos_pba.png"
import censo_agropecuario from "./assets/censo_agropecuario.png"
import jurisprudencia from "./assets/jurisprudencia.png"
import normativa_comparada from "./assets/normativa_comparada.png"


const images = {
    pis_en_humanxs,
    zonificacion_normativa,
    agroquimicos_pba,
    censo_agropecuario,
    jurisprudencia,
    normativa_comparada,

};

export default ({ data }) => {

    return (
        <section id={data.id} className={`hero tool tool-${data.color}`}>
            <div className="hero-body">
                <div className="container">
                    <div className="text-content">
                        <div className="columns">
                            <div className="column is-one-third">
                                <h4 className="title is-4 is-spaced is-size-2-desktop">{data.title}</h4>
                                <figure className="image is-hidden-desktop is-hidden-tablet">
                                    <img src={`${images[data.image]}`} alt="" />
                                </figure>
                                <p className="subtitle is-6 is-spaced">{data.description_section}</p>
                                <div className="list-wrapper">
                                    <ul className="list">
                                        {data.features.map((feature, index) =>
                                            <li key={index} className="has-text-white">{feature}</li>
                                        )}
                                    </ul>
                                </div>
                                <div className="button-container">
                                    <PopupButton id="bkXtFW" className="button is-rounded is-medium is-black" href="#implementar">implementation</PopupButton>
                                </div>
                            </div>
                            <div className="column">
                            <figure className="image is-hidden-mobile">
                                <img src={`${images[data.image]}`} alt="" />
                            </figure>
                            </div>
                        </div>
                    </div>
                </div>
            </div>    
        </section>
    )
}