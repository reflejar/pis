library(shiny)

ui <- fluidPage(
  titlePanel("Mi aplicación Shiny"),
  sidebarLayout(
    sidebarPanel(
      selectInput("variable", "Seleccione una variable:",
                  choices = colnames(mtcars)[1:3])
    ),
    mainPanel(
      plotOutput("plot")
    )
  )
)

server <- function(input, output) {
  output$plot <- renderPlot({
    plot(mtcars[, input$variable])
  })
}

# Run the application 
shinyApp(ui = ui, server = server)