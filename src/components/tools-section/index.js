import React from "react"
import "./styles.scss"

import pis_en_humanxs from "./assets/pis_en_humanxs.svg"
import zonificacion_normativa from "./assets/zonificacion_normativa.svg"
import agroquimicos_pba from "./assets/agroquimicos_pba.svg"
import censo_agropecuario from "./assets/censo_agropecuario.svg"
import jurisprudencia from "./assets/jurisprudencia.svg"
import normativa_comparada from "./assets/normativa_comparada.svg"
import caja_herramientas from "./assets/caja_herramientas.svg"


const icons = {
    pis_en_humanxs,
    zonificacion_normativa,
    agroquimicos_pba,
    censo_agropecuario,
    jurisprudencia,
    normativa_comparada,
    caja_herramientas
};

export default ({ tools }) =>  {

    return (
        <section id="herramientas" className="section">
            <div className="container">
                <div className="columns is-multiline is-mobile is-centered">
                    {tools.map((tool) =>
                        // <div key={'p-sect'+tool.id} className={`tool-item tool-item-${tool.color} column has-text-centered is-half-tablet is-half-desktop is-full-mobile`}>
                        <div key={'p-sect'+tool.id} className={`tool-item column has-text-centered is-half-tablet is-one-third-desktop is-full-mobile`}>
                            <figure className="image">
                                <img src={`${icons[tool.icon]}`} alt="" className={`${tool.icon}`} />
                            </figure>
                            <h4 className="title is-spaced has-text-white">{tool.title}</h4>
                            <p className="subtitle is-6 is-spaced has-text-white">{tool.explanation}</p>
                            <a className="icon is-large" href={`#${tool.id}`}>
                                <i className="fas fa-plus fa-inverse"></i>
                            </a>
                        </div>
                    )}
                </div>
            </div>
        </section>
    )
}