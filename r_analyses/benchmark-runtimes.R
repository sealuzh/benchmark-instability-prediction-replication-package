library("scales")
library("tidyverse")

get_measurements_file <- function() {
  col_types <- cols(
    project = col_character(),
    commit = col_character(),
    benchmark = col_character(),
    params = col_character(),
    instance = col_double(),
    trial = col_double(),
    fork = col_double(),
    iteration = col_double(),
    mode = col_character(),
    unit = col_character(),
    value_count = col_double(),
    value = col_number()
  )
  fp <- paste("data/all_measurements.csv", sep = "")
  csv <- read_delim(fp, col_types = col_types, delim = ";")
  return(csv)
}

measurements <- function(df) {
  ndf <- df %>%
    group_by(project, benchmark) %>%
    summarize(
      mean = mean(value),
      sd = sd(value),
      median = median(value),
      mad = mad(value)
    )
  return(ndf)
}

run <- function() {
  df <- measurements(get_measurements_file()) %>%
    mutate(val = round(mean)/1000000)
  
  total <- nrow(df)
  
  print(
    df %>%
      mutate(
        val_group = case_when(
          val <= 1 ~ "<=1ms",
          val <= 10 ~ "<=10ms",
          val <= 100 ~ "<=100ms",
          val <= 1000 ~ "<=1s",
          TRUE ~ ">1s"
        )
      ) %>%
      group_by(val_group) %>%
      summarize(
        count = n(),
        perc = count / total
      )
  )
  
  p <- ggplot(df, aes(x = val)) +
    geom_histogram(color="black", fill="white") +
    scale_y_continuous(trans="log10") +
    scale_x_continuous(trans="log10", labels = scales::comma) +
    ylab("# Benchmarks") +
    xlab("Mean Execution Time [ms]")
  
  ggsave(paste("figures/runtime-histogram.pdf", sep = ""), p, width = 5, height = 3)
}
