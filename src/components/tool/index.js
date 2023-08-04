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

    const showImage = () => (<div className="column">
                                <figure className="image is-hidden-mobile">
                                    <img src={`${images[data.image]}`} alt={`Imagen de ${data.title}`} />
                                </figure>
                            </div>)

    const showText = () => (<div className="column">
                                <h4 className={`title is-4 is-spaced is-size-2-desktop ${data['text_style']}`}>{data.title}</h4>
                                <p className={`subtitle is-6 is-spaced ${data['text_style']}`}>{data.description_section}</p>
                                <div className="list-wrapper">
                                    <ul className="list">
                                        {data.features.map((feature, index) =>
                                            <li key={index} className={`${data['text_style']}`}>{feature}</li>
                                        )}
                                    </ul>
                                </div>
                                <div className="button-container">
                                    <PopupButton id="" className="button is-rounded is-medium is-black" href="#implementar">Entrar</PopupButton>
                                </div>
                            </div>)


    return (
        <section id={data.id} className={`hero tool tool-${data.id}`}>
            <div className="hero-body">
                <div className="container">
                    {data.image_disposition === "left" ?   
                        <div className="columns">
                            {showImage()}
                            {showText()}
                        </div> : 
                        <div className="columns">
                            {showText()}
                            {showImage()}
                        </div>
                    }
                </div>
            </div>    
        </section>
    )
}