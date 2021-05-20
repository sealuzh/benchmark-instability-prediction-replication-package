library("tidyverse")
library("mice")
# devtools::install_github("klainfo/ScottKnottESD", ref="development")
library("ScottKnottESD")
library("rstatix")
library("effsize")

get_importance_file <- function(metric) {
  col_types <- cols(
    `dependent_variable` = col_character(),
    `iterations` = col_integer(),
    `threshold` = col_integer(),
    `selector` = col_character(),
    `model` = col_character(),
    `fold` = col_integer(),
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
  
  fp <- paste("../study/resources/feature_importance_", metric, "_results.csv", sep = "")
  csv <- read_delim(fp, col_types = col_types, delim = ",") %>%
    rename_with(~ gsub("/", "_", .x, fixed = TRUE))
  return(csv)
}

impute_data <- function(df) {
  return(mice(df, method = "norm", maxit = 50, seed = 21984646))
}

scott_knott <- function(df, version = "np", alpha = 0.01) {
  sk <- sk_esd(df, version = version, alpha = alpha)
  df_sk <- as.data.frame(sk$groups) %>%
    rownames_to_column("feature") %>%
    rename(sk = 2)
  
  # invert sk ranks
  # max <- max(df_sk %>% pull(sk))
  # df_sk <- df_sk %>% mutate(sk = max + 1 - sk)
  
  return(df_sk)
}

# mj <- function(x, weights, p, alpha) {
#   if (any(is.na(weights)))
#     weights <- rep(1 / length(x), length(x))
#   
#   indexes <- order(x)
#   x <- x[indexes]
#   weights <- weights[indexes]
#   
#   nw <- sum(weights) / max(weights)
#   a <- p * (nw + 1)
#   b <- (1 - p) * (nw + 1)
#   
#   cdfs.probs <- cumsum(c(0, weights / sum(weights)))
#   cdfs <- pbeta(cdfs.probs, a, b)
#   W <- tail(cdfs, -1) - head(cdfs, -1)
#   
#   c1 <- sum(W * x)
#   c2 <- sum(W * x^2)
#   se <- sqrt(c2 - c1^2)
#   estimation <- c1
#   margin <- se * qt(1 - (1 - alpha) / 2, df = nw - 1)
#   
#   return(paste(estimation - margin, estimation + margin, sep = ":"))
# }

proper_features <- function(labels) {
  feature <- function(labels) {
    return(str_replace_all(labels, "_", "/"))
  }
  
  return(case_when(
    str_starts(labels, "bench") ~ paste("Bench:", feature(str_replace(labels, "bench_", ""))),
    str_starts(labels, "code") ~ paste("Code:", feature(str_replace(labels, "code_", ""))),
    TRUE ~ "unknown"
  ))
}

proper_metric <- function(m) {
  nm <- switch(m,
    "mcc" = "MCC",
    "auc" = "AUC",
    "fmeasure" = "F-measure"
  )
  return(nm)
}

plot_importances <- function(df, sk_version, dep_var, metric) {
  fn <- paste("figures/individual_features/individual_feature_importances-", sk_version, "-", dep_var, "-", metric, ".pdf", sep = "")
  pd <- position_dodge(0.1)
  p <- ggplot(df, aes(x = importance, y = feature)) +
    geom_boxplot() +
    facet_grid(rows = vars(sk), scales = "free_y", space = "free_y") +
    xlab(paste("Permutation Feature Importance based on", proper_metric(metric))) +
    ylab("Feature") +
    scale_y_discrete(labels = proper_features)
  
  ggsave(fn, plot = p, width = 15, height = 30, units = "cm")
}

check_normality <- function(df, alpha = 0.05) {
  filter <- df %>%
    group_by(feature) %>%
    summarize(remove = sd(importance) == 0)
  
  df_filtered <- df %>%
    inner_join(filter, by = c("feature")) %>%
    filter(remove != TRUE) %>%
    select(-remove)
  
  df_normality <- df_filtered %>%
    group_by(feature) %>%
    shapiro_test(importance) %>%
    mutate(`non-normal` = p < alpha)
  
  df_normality_summary <- df_normality %>%
    group_by(`non-normal`) %>%
    summarize(count = n())
  
  print(paste("features in df:", nrow(df %>% group_by(feature) %>% summarize(median = median(importance)))))
  print(paste("features removed for Shapiro-Wilk test:", nrow(filter %>% filter(remove == TRUE))))
  print(df_normality_summary)
}

run_scott_knott <- function(df, dep_var, metric, plot) {
  l <- NULL
  
  imp_data <- impute_data(df)
  
  df_imp <- complete(imp_data) %>%
    mutate(across(where(~any(is.na(.x))), ~if_else(is.na(.x), 0.0, .x)))
  
  df_imp_long <- df_imp %>%
    mutate(row_id = row_number()) %>%
    pivot_longer(-row_id, names_to = "feature", values_to = "importance")
  
  check_normality(df_imp_long)
  
  l$imputed <- df_imp_long
  
  # sk_versions <- c("p", "np")
  sk_versions <- c("np")
  
  for (sk_version in sk_versions) {
    df_sk <- scott_knott(df_imp, version = sk_version)

    df_features_ranked <- inner_join(df_imp_long, df_sk, by = "feature")

    df_summary <- df_features_ranked %>%
      group_by(feature) %>%
      summarize(importance_median = median(importance)) %>%
      ungroup() %>%
      arrange(-importance_median, feature) %>%
      mutate(order = row_number()) %>%
      select(feature, order)

    df_ordered <- inner_join(df_features_ranked, df_summary, by = c("feature")) %>%
      mutate(feature = fct_reorder(feature, -order)) %>%
      select(-order)
    
    l[[paste("sk_version", sk_version, sep = "_")]] <- df_ordered

    if (plot == TRUE) {
      plot_importances(df_ordered, sk_version = sk_version, dep_var = dep_var, metric = metric)
    }
  }
  return(l)
}

run <- function(plot = TRUE) {
  l <- NULL
  metrics <- c("mcc", "auc", "fmeasure")
  # metrics <- c("mcc")
  dep_vars <- c("rciw99", "rciw99mjhd", "rmadhd")
  # dep_vars <- c("rciw99mjhd")
  
  for (metric in metrics) {
    df <- get_importance_file(metric = metric)
    
    for (dep_var in dep_vars) {
      print(paste("run dep_var=", dep_var, " and metric=", metric, sep = ""))
      
      df_only_features <- df %>%
        filter(`dependent_variable` == dep_var) %>%
        select(-c("dependent_variable", "iterations", "threshold", "selector", "model", "fold")) %>%
        select_if(~sum(!is.na(.)) > 0)
      
      ret <- run_scott_knott(df_only_features, dep_var = dep_var, metric = metric, plot = plot)
      l[[metric]][[dep_var]] <- ret
    }
  }
  df_sk <<- l
}

run_individual_features_stats <- function() {
  digits <- 5
  df_features <- df_sk$mcc$rciw99mjhd$sk_version_np
  stats_df <- df_features %>%
      group_by(feature) %>%
      summarize(
        importance_median = round(median(importance), digits = digits),
        importance_mad = round(mad(importance), digits = digits),
        importance_iqr = round(IQR(importance), digits = digits),
        importance_quantile_25 = round(quantile(importance, 0.25), digits = 5),
        importance_quantile_75 = round(quantile(importance, 0.75), digits = 5),
        sk = first(sk)
      ) %>%
      ungroup() %>%
      arrange(sk, -importance_median)
  
  View(stats_df)
}
