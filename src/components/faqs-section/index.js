import React from "react"
import "./styles.scss"
import { PopupButton } from '@typeform/embed-react'

import diy from "./assets/diy.svg"
import standard from "./assets/standard.svg"
import custom from "./assets/custom.svg"

import data from "./content.json"

const icons = {
    diy,
    custom,
    standard
};

export default () => {

    return (
        <section id="implementar" className="section faqs">
            <div className="container has-text-centered">
                <h3 className="main-title title is-4 is-size-1-desktop">{data.title }</h3>
                <div className="columns has-text-left">
                    {data.faqs.map((instalation, index) =>
                        <div key={index} className="column">
                            <figure className="image">
                                <img src={`${icons[instalation.icon]}`} className={`${instalation.icon}`} alt="" />
                            </figure>
                            <div className="text-wrapper">
                                <h4 className="title is-4 is-spaced">{instalation.title}</h4>
                                <p className="subtitle is-6 is-spaced">{instalation.description}</p>
                            </div>
                            <div className="list-wrapper">
                                <span className="list-title">requirements</span>
                                <ul className="list">
                                    {instalation.requirements.map((requirement, index) =>
                                        <li key={index}>{requirement}</li>
                                    )}
                                </ul>
                            </div>
                            {index === 0 ?
                                <a className="button is-rounded is-medium is-dark" href={instalation.button_link} target="_blank" rel="noopener noreferrer">{instalation.button_text}</a>
                                :
                                <PopupButton id="bkXtFW" className="button is-rounded is-medium is-dark" rel="noopener noreferrer">{instalation.button_text}</PopupButton>
                            }
                        </div>
                    )}
                </div>
            </div>
        </section>
    )
}