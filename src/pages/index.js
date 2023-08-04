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

import toolsData from "./tools.json"
// import faqsData from "../../content/faqs.json"
// import donateData from "../../content/donar.json"

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
        <HeroSlider/>
        <ToolsSection tools={toolsData}/>
        {toolsData.filter((tool) => tool.description_section !== "").sort((a, b) => a.order - b.order).map((tool) => 
            <Tool data={tool} key={'prod-d'+tool.id}/>
        )}
        {/* <FAQsSection />     */}
        {/* <DonateSection data={donateData}/> */}
        <UsSection/>
        <WorkWithSection />
        <Footer />
    </React.Fragment>
    )

}

export default Home;
