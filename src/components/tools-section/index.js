import React from "react"
import "./styles.scss"

import consulta_publica from "./assets/consulta_publica.svg"
import co_construccion from "./assets/co_construccion.svg"
import presupuesto_participativo from "./assets/presupuesto_participativo.svg"
import seguimiento_metas from "./assets/seguimiento_metas.svg"
import votacion_autoridades from "./assets/votacion_autoridades.svg"


const icons = {
    consulta_publica,
    co_construccion,
    presupuesto_participativo,
    seguimiento_metas,
    votacion_autoridades,
};

export default ({ tools }) =>  {

    return (
        <section id="herramientas" className="section">
            <div className="container">
                <div className="columns is-multiline is-mobile is-centered">
                    {tools.map((tool) =>
                        // <div key={'p-sect'+tool.id} className={`tool-item tool-item-${tool.color} column has-text-centered is-half-tablet is-half-desktop is-full-mobile`}>
                        <div key={'p-sect'+tool.id} className={`tool-item column has-text-centered is-half-tablet is-half-desktop is-full-mobile`}>
                            <figure className="image">
                                <img src={`${icons[tool.icon]}`} alt="" className={`${tool.icon}`} />
                            </figure>
                            <h4 className="title is-spaced has-text-grey-dark">{tool.title}</h4>
                            <p className="subtitle is-6 is-spaced has-text-grey-dark">{tool.explanation}</p>
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