library("scales")
library("tidyverse")

get_variabilities_file <- function(iterations) {
  fp <- paste("../study/resources/variabilities_", iterations, "_iterations.csv", sep = "")
  
  col_types <- cols(
    `project_name` = col_character(),
    `function` = col_character(),
    `executions` = col_integer(),
    `mean` = col_double(),
    `cv` = col_double(),
    `rciw95` = col_double(),
    `rciw99` = col_double(),
    `rciw99mjhd` = col_double(),
    `rmad` = col_double(),
    `rmadhd` = col_double(),
    `bench_fileloc` = col_double(),
    `bench_pkgfiles` = col_double(),
    `bench_loc` = col_double(),
    `bench_namelength` = col_double(),
    `bench_parameters` = col_double(),
    `bench_ifelses` = col_double(),
    `bench_switches` = col_double(),
    `bench_switchcases` = col_double(),
    `bench_loops` = col_double(),
    `bench_nestedloops` = col_double(),
    `bench_funccalls` = col_double(),
    `bench_returns` = col_double(),
    `bench_defers` = col_double(),
    `bench_panics` = col_double(),
    `bench_recovers` = col_double(),
    `bench_cyclomaticcomplexity` = col_double(),
    `bench_variables` = col_double(),
    `bench_pointers` = col_double(),
    `bench_slices` = col_double(),
    `bench_maps` = col_double(),
    `bench_gos` = col_double(),
    `bench_channels` = col_double(),
    `bench_sends` = col_double(),
    `bench_receives` = col_double(),
    `bench_closes` = col_double(),
    `bench_concrranges` = col_double(),
    `bench_selects` = col_double(),
    `bench_selectcases` = col_double(),
    `bench_bufio` = col_double(),
    `bench_bytes` = col_double(),
    `bench_crypto` = col_double(),
    `bench_database/sql` = col_double(),
    `bench_encoding` = col_double(),
    `bench_encoding/binary` = col_double(),
    `bench_encoding/csv` = col_double(),
    `bench_encoding/json` = col_double(),
    `bench_encoding/xml` = col_double(),
    `bench_io` = col_double(),
    `bench_io/ioutil` = col_double(),
    `bench_math` = col_double(),
    `bench_math/rand` = col_double(),
    `bench_mime` = col_double(),
    `bench_net` = col_double(),
    `bench_net/http` = col_double(),
    `bench_net/http/httptest` = col_double(),
    `bench_net/http/httptrace` = col_double(),
    `bench_net/http/httputil` = col_double(),
    `bench_net/rpc` = col_double(),
    `bench_net/rpc/jsonrpc` = col_double(),
    `bench_net/smtp` = col_double(),
    `bench_net/textproto` = col_double(),
    `bench_os` = col_double(),
    `bench_os/exec` = col_double(),
    `bench_os/signal` = col_double(),
    `bench_sort` = col_double(),
    `bench_strconv` = col_double(),
    `bench_sync` = col_double(),
    `bench_sync/atomic` = col_double(),
    `bench_syscall` = col_double(),
    `code_fileloc` = col_double(),
    `code_pkgfiles` = col_double(),
    `code_loc` = col_double(),
    `code_namelength` = col_double(),
    `code_parameters` = col_double(),
    `code_ifelses` = col_double(),
    `code_switches` = col_double(),
    `code_switchcases` = col_double(),
    `code_loops` = col_double(),
    `code_nestedloops` = col_double(),
    `code_funccalls` = col_double(),
    `code_returns` = col_double(),
    `code_defers` = col_double(),
    `code_panics` = col_double(),
    `code_recovers` = col_double(),
    `code_cyclomaticcomplexity` = col_double(),
    `code_variables` = col_double(),
    `code_pointers` = col_double(),
    `code_slices` = col_double(),
    `code_maps` = col_double(),
    `code_gos` = col_double(),
    `code_channels` = col_double(),
    `code_sends` = col_double(),
    `code_receives` = col_double(),
    `code_closes` = col_double(),
    `code_concrranges` = col_double(),
    `code_selects` = col_double(),
    `code_selectcases` = col_double(),
    `code_bufio` = col_double(),
    `code_bytes` = col_double(),
    `code_crypto` = col_double(),
    `code_database/sql` = col_double(),
    `code_encoding` = col_double(),
    `code_encoding/binary` = col_double(),
    `code_encoding/csv` = col_double(),
    `code_encoding/json` = col_double(),
    `code_encoding/xml` = col_double(),
    `code_io` = col_double(),
    `code_io/ioutil` = col_double(),
    `code_math` = col_double(),
    `code_math/rand` = col_double(),
    `code_mime` = col_double(),
    `code_net` = col_double(),
    `code_net/http` = col_double(),
    `code_net/http/httptest` = col_double(),
    `code_net/http/httptrace` = col_double(),
    `code_net/http/httputil` = col_double(),
    `code_net/rpc` = col_double(),
    `code_net/rpc/jsonrpc` = col_double(),
    `code_net/smtp` = col_double(),
    `code_net/textproto` = col_double(),
    `code_os` = col_double(),
    `code_os/exec` = col_double(),
    `code_os/signal` = col_double(),
    `code_sort` = col_double(),
    `code_strconv` = col_double(),
    `code_sync` = col_double(),
    `code_sync/atomic` = col_double(),
    `code_syscall` = col_double()
  )
  
  csv <- read_delim(fp, col_types = col_types, delim = ",") %>%
    select(-c(cv, rciw95, rmad))
  return(csv)
}

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

get_plot <- function(df, x, y, xlab = x, ylab = y, xlabels = waiver(), ylabels = scales::comma) {
  p <- ggplot(df, aes_string(x = x, y = y)) +
    scale_y_continuous(trans="log10", labels = ylabels) +
    scale_x_continuous(trans="log10", labels = xlabels) +
    geom_point(alpha = 0.6) +
    ylab(ylab) +
    xlab(xlab)
  return(p)
}

run <- function() {
  iterations <- c(5, 10, 20, 30)
  dependant_variables <- c("rciw99", "rciw99mjhd", "rmadhd")
  dependant_variables_regex <- c("^rciw99$", "^rciw99mjhd$", "^rmadhd$")
  ylabs <- c("RCIW Bootstrap [%]", "RCIW Maritz-Jarrett [%]", "RMAD Harrell-Davis [%]")
  
  df_bench_iters <- get_measurements_file() %>%
    group_by(project, benchmark) %>%
    summarize(max_iterations = n())
  
  for (dv_idx in 1:length(dependant_variables)) {
    dv <- dependant_variables[[dv_idx]]
    dv_regex <- dependant_variables_regex[[dv_idx]]
    ylab <- ylabs[[dv_idx]]
    
    for (i in iterations) {
      df <- get_variabilities_file(i) %>%
        rename(dv = matches(dv_regex)) %>%
        # mutate(dv = dv / 100) %>%
        rename(
          benchmark = `function`,
          project = project_name
        ) %>%
        select(project, benchmark, executions, mean, dv) #%>%
        # filter(mean != 0 | rciw99 != 0)
     
      # mean to rciw scatter plot 
      p1 <- get_plot(df, x = "mean", y = "dv", xlab = "Mean Runtime [ns]", ylab = ylab)
      
      ggsave(paste("figures/variability-iterations/scatter-", i, "_iterations-", dv, "-mean.pdf", sep = ""), p1, width = 5, height = 3)
      
      # max iterations to rciw scatter plot
      df_2 <- df %>% left_join(df_bench_iters, by = c("project", "benchmark"))
      
      p2 <- get_plot(df_2, "max_iterations", "dv", xlab = "Maximum Iterations", ylab = ylab, xlabels = scales::comma)
      
      ggsave(paste("figures/variability-iterations/scatter-", i, "_iterations-", dv, "-max_iterations.pdf", sep = ""), p2, width = 5, height = 3)
    }
  }
}

## helper analyses

run_unstable_benchmarks<- function() {
  iterations <- c(5, 10, 20, 30)
  dependant_variables <- c("cv", "rciw99", "rmad")
  thresholds <- c(1, 3, 5, 10)
  
  
  for (dv_idx in 1:length(dependant_variables)) {
    dv <- dependant_variables[[dv_idx]]
    
    for (i in iterations) {
      
      for (t in thresholds) {
        df <- get_variabilities_file(i) %>%
          rename(dv = contains(dv)) %>%
          mutate(dv = dv) %>%
          rename(
            benchmark = `function`,
            project = project_name
          ) %>%
          select(project, benchmark, executions, mean, dv) #%>%
        # filter(mean != 0 | rciw99 != 0)
        
        print(paste("dep var=", dv, "; iter=", i, "; thresh=", t, sep = ""))
        print(paste("total=", nrow(df), "; unstable=", nrow(df %>% filter(dv >= t)), sep = ""))
      }
    }
  }
}
