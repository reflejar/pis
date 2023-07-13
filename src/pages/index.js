import React from "react"
import "./styles.scss"

import SEO from "../components/seo"
import Navbar from "../components/navbar"
import HeroSlider from "../components/hero-slider"
import ToolsSection from "../components/tools-section"
import Tool from "../components/tool"
import FAQsSection from "../components/faqs-section"
import UsSection from "../components/us-section"
import DonateSection from "../components/donate-section"
import Footer from "../components/footer"
import WorkWithSection from "../components/work-with-section"

import heroSliderData from "../../content/hero-slider.json"
import toolsData from "../../content/tools.json"
import faqsData from "../../content/faqs.json"
import usData from "../../content/nosotros.json"
import donateData from "../../content/donar.json"

//Sets smooth scroll animation for anchor links
if (typeof window !== "undefined") {
    const SmoothScroll = require("smooth-scroll");
    new SmoothScroll('a[href*="#"]');
}

const Home = () => {
    return (
    <React.Fragment>
        <SEO />
        <Navbar/>
        <HeroSlider slides={heroSliderData}/>
        <ToolsSection tools={toolsData}/>
        {toolsData.map((tool) => 
            <Tool data={tool} key={'prod-d'+tool.id}/>
        )}
        <FAQsSection data={faqsData}/>    
        <DonateSection data={donateData}/>
        <UsSection data={usData}/>
        <WorkWithSection />
        <Footer />
    </React.Fragment>
    )

}

export default Home;
