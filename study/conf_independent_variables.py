import itertools



# Independent variable names.

IV_BENCH_FILELOC = 'bench_fileloc'
IV_BENCH_PKGFILES = 'bench_pkgfiles'
IV_BENCH_LOC = 'bench_loc'
IV_BENCH_NAMELENGTH = 'bench_namelength'
IV_BENCH_PARAMS = 'bench_parameters'

IV_BENCH_IFS = 'bench_ifelses'
IV_BENCH_SWITCHES = 'bench_switches'
IV_BENCH_SWITCHCASES = 'bench_switchcases'
IV_BENCH_LOOPS = 'bench_loops'
IV_BENCH_NESTEDLOOPS = 'bench_nestedloops'
IV_BENCH_FUNCCALLS = 'bench_funccalls'
IV_BENCH_RETS = 'bench_returns'
IV_BENCH_DEFERS = 'bench_defers'
IV_BENCH_PANICS = 'bench_panics'
IV_BENCH_RECOVERS = 'bench_recovers'
IV_BENCH_CC = 'bench_cyclomaticcomplexity'

IV_BENCH_VARS = 'bench_variables'
IV_BENCH_PTRS = 'bench_pointers'
IV_BENCH_SLICES = 'bench_slices'
IV_BENCH_MAPS = 'bench_maps'

IV_BENCH_GOS = 'bench_gos'
IV_BENCH_CHANNELS = 'bench_channels'
IV_BENCH_CHSENDS = 'bench_sends'
IV_BENCH_CHRECS = 'bench_receives'
IV_BENCH_CHCLOSES = 'bench_closes'
IV_BENCH_CHRANGES = 'bench_concrranges'
IV_BENCH_SELECTS = 'bench_selects'
IV_BENCH_SELECTCASES = 'bench_selectcases'

IV_BENCH_STDLIB_BUFIO = 'bench_bufio'
IV_BENCH_STDLIB_BYTES = 'bench_bytes'
IV_BENCH_STDLIB_CRYPTO = 'bench_crypto'
IV_BENCH_STDLIB_DATABASE_SQL = 'bench_database/sql'
IV_BENCH_STDLIB_ENCODING = 'bench_encoding'
IV_BENCH_STDLIB_ENCODING_BINARY = 'bench_encoding/binary'
IV_BENCH_STDLIB_ENCODING_CSV = 'bench_encoding/csv'
IV_BENCH_STDLIB_ENCODING_JSON = 'bench_encoding/json'
IV_BENCH_STDLIB_ENCODING_XML = 'bench_encoding/xml'
IV_BENCH_STDLIB_IO = 'bench_io'
IV_BENCH_STDLIB_IO_IOUTIL = 'bench_io/ioutil'
IV_BENCH_STDLIB_MATH = 'bench_math'
IV_BENCH_STDLIB_MATH_RAND = 'bench_math/rand'
IV_BENCH_STDLIB_MIME = 'bench_mime'
IV_BENCH_STDLIB_NET = 'bench_net'
IV_BENCH_STDLIB_NET_HTTP = 'bench_net/http'
IV_BENCH_STDLIB_NET_HTTP_HTTPTEST = 'bench_net/http/httptest'
IV_BENCH_STDLIB_NET_HTTP_HTTPTRACE = 'bench_net/http/httptrace'
IV_BENCH_STDLIB_NET_HTTP_HTTPUTIL = 'bench_net/http/httputil'
IV_BENCH_STDLIB_NET_RPC = 'bench_net/rpc'
IV_BENCH_STDLIB_NET_RPC_JSONRPC = 'bench_net/rpc/jsonrpc'
IV_BENCH_STDLIB_NET_SMTP = 'bench_net/smtp'
IV_BENCH_STDLIB_NET_TEXTPROTO = 'bench_net/textproto'
IV_BENCH_STDLIB_OS = 'bench_os'
IV_BENCH_STDLIB_OS_EXEC = 'bench_os/exec'
IV_BENCH_STDLIB_OS_SIGNAL = 'bench_os/signal'
IV_BENCH_STDLIB_SORT = 'bench_sort'
IV_BENCH_STDLIB_STRCONV = 'bench_strconv'
IV_BENCH_STDLIB_SYNC = 'bench_sync'
IV_BENCH_STDLIB_SYNC_ATOMIC = 'bench_sync/atomic'
IV_BENCH_STDLIB_SYSCALL = 'bench_syscall'


IV_CODE_FILELOC = 'code_fileloc'
IV_CODE_PKGFILES = 'code_pkgfiles'
IV_CODE_LOC = 'code_loc'
IV_CODE_NAMELENGTH = 'code_namelength'
IV_CODE_PARAMS = 'code_parameters'

IV_CODE_IFS = 'code_ifelses'
IV_CODE_SWITCHES = 'code_switches'
IV_CODE_SWITCHCASES = 'code_switchcases'
IV_CODE_LOOPS = 'code_loops'
IV_CODE_NESTEDLOOPS = 'code_nestedloops'
IV_CODE_FUNCCALLS = 'code_funccalls'
IV_CODE_RETS = 'code_returns'
IV_CODE_DEFERS = 'code_defers'
IV_CODE_PANICS = 'code_panics'
IV_CODE_RECOVERS = 'code_recovers'
IV_CODE_CC = 'code_cyclomaticcomplexity'

IV_CODE_VARS = 'code_variables'
IV_CODE_PTRS = 'code_pointers'
IV_CODE_SLICES = 'code_slices'
IV_CODE_MAPS = 'code_maps'

IV_CODE_GOS = 'code_gos'
IV_CODE_CHANNELS = 'code_channels'
IV_CODE_CHSENDS = 'code_sends'
IV_CODE_CHRECS = 'code_receives'
IV_CODE_CHCLOSES = 'code_closes'
IV_CODE_CHRANGES = 'code_concrranges'
IV_CODE_SELECTS = 'code_selects'
IV_CODE_SELECTCASES = 'code_selectcases'

IV_CODE_STDLIB_BUFIO = 'code_bufio'
IV_CODE_STDLIB_BYTES = 'code_bytes'
IV_CODE_STDLIB_CRYPTO = 'code_crypto'
IV_CODE_STDLIB_DATABASE_SQL = 'code_database/sql'
IV_CODE_STDLIB_ENCODING = 'code_encoding'
IV_CODE_STDLIB_ENCODING_BINARY = 'code_encoding/binary'
IV_CODE_STDLIB_ENCODING_CSV = 'code_encoding/csv'
IV_CODE_STDLIB_ENCODING_JSON = 'code_encoding/json'
IV_CODE_STDLIB_ENCODING_XML = 'code_encoding/xml'
IV_CODE_STDLIB_IO = 'code_io'
IV_CODE_STDLIB_IO_IOUTIL = 'code_io/ioutil'
IV_CODE_STDLIB_MATH = 'code_math'
IV_CODE_STDLIB_MATH_RAND = 'code_math/rand'
IV_CODE_STDLIB_MIME = 'code_mime'
IV_CODE_STDLIB_NET = 'code_net'
IV_CODE_STDLIB_NET_HTTP = 'code_net/http'
IV_CODE_STDLIB_NET_HTTP_HTTPTEST = 'code_net/http/httptest'
IV_CODE_STDLIB_NET_HTTP_HTTPTRACE = 'code_net/http/httptrace'
IV_CODE_STDLIB_NET_HTTP_HTTPUTIL = 'code_net/http/httputil'
IV_CODE_STDLIB_NET_RPC = 'code_net/rpc'
IV_CODE_STDLIB_NET_RPC_JSONRPC = 'code_net/rpc/jsonrpc'
IV_CODE_STDLIB_NET_SMTP = 'code_net/smtp'
IV_CODE_STDLIB_NET_TEXTPROTO = 'code_net/textproto'
IV_CODE_STDLIB_OS = 'code_os'
IV_CODE_STDLIB_OS_EXEC = 'code_os/exec'
IV_CODE_STDLIB_OS_SIGNAL = 'code_os/signal'
IV_CODE_STDLIB_SORT = 'code_sort'
IV_CODE_STDLIB_STRCONV = 'code_strconv'
IV_CODE_STDLIB_SYNC = 'code_sync'
IV_CODE_STDLIB_SYNC_ATOMIC = 'code_sync/atomic'
IV_CODE_STDLIB_SYSCALL = 'code_syscall'


INDEPENDENT_VARIABLES = [
    # Benchmark features.
    IV_BENCH_FILELOC, IV_BENCH_PKGFILES, IV_BENCH_LOC, IV_BENCH_NAMELENGTH, IV_BENCH_PARAMS, IV_BENCH_IFS, IV_BENCH_SWITCHES, IV_BENCH_SWITCHCASES, IV_BENCH_LOOPS, IV_BENCH_NESTEDLOOPS, IV_BENCH_FUNCCALLS, IV_BENCH_RETS, IV_BENCH_DEFERS, IV_BENCH_PANICS, IV_BENCH_RECOVERS, IV_BENCH_CC, IV_BENCH_VARS, IV_BENCH_PTRS, IV_BENCH_SLICES, IV_BENCH_MAPS, IV_BENCH_GOS, IV_BENCH_CHANNELS, IV_BENCH_CHSENDS, IV_BENCH_CHRECS, IV_BENCH_CHCLOSES, IV_BENCH_CHRANGES, IV_BENCH_SELECTS, IV_BENCH_SELECTCASES,
    IV_BENCH_STDLIB_BUFIO, IV_BENCH_STDLIB_BYTES, IV_BENCH_STDLIB_CRYPTO, IV_BENCH_STDLIB_DATABASE_SQL, IV_BENCH_STDLIB_ENCODING, IV_BENCH_STDLIB_ENCODING_BINARY, IV_BENCH_STDLIB_ENCODING_CSV, IV_BENCH_STDLIB_ENCODING_JSON, IV_BENCH_STDLIB_ENCODING_XML, IV_BENCH_STDLIB_IO, IV_BENCH_STDLIB_IO_IOUTIL, IV_BENCH_STDLIB_MATH, IV_BENCH_STDLIB_MATH_RAND, IV_BENCH_STDLIB_MIME, IV_BENCH_STDLIB_NET, IV_BENCH_STDLIB_NET_HTTP, IV_BENCH_STDLIB_NET_HTTP_HTTPTEST, IV_BENCH_STDLIB_NET_HTTP_HTTPTRACE, IV_BENCH_STDLIB_NET_HTTP_HTTPUTIL, IV_BENCH_STDLIB_NET_RPC, IV_BENCH_STDLIB_NET_RPC_JSONRPC, IV_BENCH_STDLIB_NET_SMTP, IV_BENCH_STDLIB_NET_TEXTPROTO, IV_BENCH_STDLIB_OS, IV_BENCH_STDLIB_OS_EXEC, IV_BENCH_STDLIB_OS_SIGNAL, IV_BENCH_STDLIB_SORT, IV_BENCH_STDLIB_STRCONV, IV_BENCH_STDLIB_SYNC, IV_BENCH_STDLIB_SYNC_ATOMIC, IV_BENCH_STDLIB_SYSCALL,
    
    # Code features.
    IV_CODE_FILELOC, IV_CODE_PKGFILES, IV_CODE_LOC, IV_CODE_NAMELENGTH, IV_CODE_PARAMS, IV_CODE_IFS, IV_CODE_SWITCHES, IV_CODE_SWITCHCASES, IV_CODE_LOOPS, IV_CODE_NESTEDLOOPS, IV_CODE_FUNCCALLS, IV_CODE_RETS, IV_CODE_DEFERS, IV_CODE_PANICS, IV_CODE_RECOVERS, IV_CODE_CC, IV_CODE_VARS, IV_CODE_PTRS, IV_CODE_SLICES, IV_CODE_MAPS, IV_CODE_GOS, IV_CODE_CHANNELS, IV_CODE_CHSENDS, IV_CODE_CHRECS, IV_CODE_CHCLOSES, IV_CODE_CHRANGES, IV_CODE_SELECTS, IV_CODE_SELECTCASES,
    IV_CODE_STDLIB_BUFIO, IV_CODE_STDLIB_BYTES, IV_CODE_STDLIB_CRYPTO, IV_CODE_STDLIB_DATABASE_SQL, IV_CODE_STDLIB_ENCODING, IV_CODE_STDLIB_ENCODING_BINARY, IV_CODE_STDLIB_ENCODING_CSV, IV_CODE_STDLIB_ENCODING_JSON, IV_CODE_STDLIB_ENCODING_XML, IV_CODE_STDLIB_IO, IV_CODE_STDLIB_IO_IOUTIL, IV_CODE_STDLIB_MATH, IV_CODE_STDLIB_MATH_RAND, IV_CODE_STDLIB_MIME, IV_CODE_STDLIB_NET, IV_CODE_STDLIB_NET_HTTP, IV_CODE_STDLIB_NET_HTTP_HTTPTEST, IV_CODE_STDLIB_NET_HTTP_HTTPTRACE, IV_CODE_STDLIB_NET_HTTP_HTTPUTIL, IV_CODE_STDLIB_NET_RPC, IV_CODE_STDLIB_NET_RPC_JSONRPC, IV_CODE_STDLIB_NET_SMTP, IV_CODE_STDLIB_NET_TEXTPROTO, IV_CODE_STDLIB_OS, IV_CODE_STDLIB_OS_EXEC, IV_CODE_STDLIB_OS_SIGNAL, IV_CODE_STDLIB_SORT, IV_CODE_STDLIB_STRCONV, IV_CODE_STDLIB_SYNC, IV_CODE_STDLIB_SYNC_ATOMIC, IV_CODE_STDLIB_SYSCALL,
]


# Independent variable groups.

IV_GROUP_BENCH = (
    'iv_group_bench',
    [
        IV_BENCH_FILELOC, IV_BENCH_PKGFILES, IV_BENCH_LOC, IV_BENCH_NAMELENGTH, IV_BENCH_PARAMS, IV_BENCH_IFS, IV_BENCH_SWITCHES, IV_BENCH_SWITCHCASES, IV_BENCH_LOOPS, IV_BENCH_NESTEDLOOPS, IV_BENCH_FUNCCALLS, IV_BENCH_RETS, IV_BENCH_DEFERS, IV_BENCH_PANICS, IV_BENCH_RECOVERS, IV_BENCH_CC, IV_BENCH_VARS, IV_BENCH_PTRS, IV_BENCH_SLICES, IV_BENCH_MAPS, IV_BENCH_GOS, IV_BENCH_CHANNELS, IV_BENCH_CHSENDS, IV_BENCH_CHRECS, IV_BENCH_CHCLOSES, IV_BENCH_CHRANGES, IV_BENCH_SELECTS, IV_BENCH_SELECTCASES,
        IV_BENCH_STDLIB_BUFIO, IV_BENCH_STDLIB_BYTES, IV_BENCH_STDLIB_CRYPTO, IV_BENCH_STDLIB_DATABASE_SQL, IV_BENCH_STDLIB_ENCODING, IV_BENCH_STDLIB_ENCODING_BINARY, IV_BENCH_STDLIB_ENCODING_CSV, IV_BENCH_STDLIB_ENCODING_JSON, IV_BENCH_STDLIB_ENCODING_XML, IV_BENCH_STDLIB_IO, IV_BENCH_STDLIB_IO_IOUTIL, IV_BENCH_STDLIB_MATH, IV_BENCH_STDLIB_MATH_RAND, IV_BENCH_STDLIB_MIME, IV_BENCH_STDLIB_NET, IV_BENCH_STDLIB_NET_HTTP, IV_BENCH_STDLIB_NET_HTTP_HTTPTEST, IV_BENCH_STDLIB_NET_HTTP_HTTPTRACE, IV_BENCH_STDLIB_NET_HTTP_HTTPUTIL, IV_BENCH_STDLIB_NET_RPC, IV_BENCH_STDLIB_NET_RPC_JSONRPC, IV_BENCH_STDLIB_NET_SMTP, IV_BENCH_STDLIB_NET_TEXTPROTO, IV_BENCH_STDLIB_OS, IV_BENCH_STDLIB_OS_EXEC, IV_BENCH_STDLIB_OS_SIGNAL, IV_BENCH_STDLIB_SORT, IV_BENCH_STDLIB_STRCONV, IV_BENCH_STDLIB_SYNC, IV_BENCH_STDLIB_SYNC_ATOMIC, IV_BENCH_STDLIB_SYSCALL,
    ],
)

IV_GROUP_CODE = (
    'iv_group_code',
    [
        IV_CODE_FILELOC, IV_CODE_PKGFILES, IV_CODE_LOC, IV_CODE_NAMELENGTH, IV_CODE_PARAMS, IV_CODE_IFS, IV_CODE_SWITCHES, IV_CODE_SWITCHCASES, IV_CODE_LOOPS, IV_CODE_NESTEDLOOPS, IV_CODE_FUNCCALLS, IV_CODE_RETS, IV_CODE_DEFERS, IV_CODE_PANICS, IV_CODE_RECOVERS, IV_CODE_CC, IV_CODE_VARS, IV_CODE_PTRS, IV_CODE_SLICES, IV_CODE_MAPS, IV_CODE_GOS, IV_CODE_CHANNELS, IV_CODE_CHSENDS, IV_CODE_CHRECS, IV_CODE_CHCLOSES, IV_CODE_CHRANGES, IV_CODE_SELECTS, IV_CODE_SELECTCASES,
        IV_CODE_STDLIB_BUFIO, IV_CODE_STDLIB_BYTES, IV_CODE_STDLIB_CRYPTO, IV_CODE_STDLIB_DATABASE_SQL, IV_CODE_STDLIB_ENCODING, IV_CODE_STDLIB_ENCODING_BINARY, IV_CODE_STDLIB_ENCODING_CSV, IV_CODE_STDLIB_ENCODING_JSON, IV_CODE_STDLIB_ENCODING_XML, IV_CODE_STDLIB_IO, IV_CODE_STDLIB_IO_IOUTIL, IV_CODE_STDLIB_MATH, IV_CODE_STDLIB_MATH_RAND, IV_CODE_STDLIB_MIME, IV_CODE_STDLIB_NET, IV_CODE_STDLIB_NET_HTTP, IV_CODE_STDLIB_NET_HTTP_HTTPTEST, IV_CODE_STDLIB_NET_HTTP_HTTPTRACE, IV_CODE_STDLIB_NET_HTTP_HTTPUTIL, IV_CODE_STDLIB_NET_RPC, IV_CODE_STDLIB_NET_RPC_JSONRPC, IV_CODE_STDLIB_NET_SMTP, IV_CODE_STDLIB_NET_TEXTPROTO, IV_CODE_STDLIB_OS, IV_CODE_STDLIB_OS_EXEC, IV_CODE_STDLIB_OS_SIGNAL, IV_CODE_STDLIB_SORT, IV_CODE_STDLIB_STRCONV, IV_CODE_STDLIB_SYNC, IV_CODE_STDLIB_SYNC_ATOMIC, IV_CODE_STDLIB_SYSCALL,
    ],
)

IV_GROUP_META = (
    'iv_group_meta',
    [
        IV_BENCH_FILELOC, IV_BENCH_PKGFILES, IV_BENCH_LOC, IV_BENCH_NAMELENGTH, IV_BENCH_PARAMS,
        IV_CODE_FILELOC, IV_CODE_PKGFILES, IV_CODE_LOC, IV_CODE_NAMELENGTH, IV_CODE_PARAMS,
    ],
)

IV_GROUP_PL = (
    'iv_group_pl',
    [
        IV_BENCH_IFS, IV_BENCH_SWITCHES, IV_BENCH_SWITCHCASES, IV_BENCH_LOOPS, IV_BENCH_NESTEDLOOPS, IV_BENCH_FUNCCALLS, IV_BENCH_RETS, IV_BENCH_DEFERS, IV_BENCH_PANICS, IV_BENCH_RECOVERS, IV_BENCH_CC, IV_BENCH_VARS, IV_BENCH_PTRS, IV_BENCH_SLICES, IV_BENCH_MAPS, IV_BENCH_GOS, IV_BENCH_CHANNELS, IV_BENCH_CHSENDS, IV_BENCH_CHRECS, IV_BENCH_CHCLOSES, IV_BENCH_CHRANGES, IV_BENCH_SELECTS, IV_BENCH_SELECTCASES,
        IV_CODE_IFS, IV_CODE_SWITCHES, IV_CODE_SWITCHCASES, IV_CODE_LOOPS, IV_CODE_NESTEDLOOPS, IV_CODE_FUNCCALLS, IV_CODE_RETS, IV_CODE_DEFERS, IV_CODE_PANICS, IV_CODE_RECOVERS, IV_CODE_CC, IV_CODE_VARS, IV_CODE_PTRS, IV_CODE_SLICES, IV_CODE_MAPS, IV_CODE_GOS, IV_CODE_CHANNELS, IV_CODE_CHSENDS, IV_CODE_CHRECS, IV_CODE_CHCLOSES, IV_CODE_CHRANGES, IV_CODE_SELECTS, IV_CODE_SELECTCASES,
    ],
)

IV_GROUP_PL_CF = (
    'iv_group_pl_cf',
    [
        IV_BENCH_IFS, IV_BENCH_SWITCHES, IV_BENCH_SWITCHCASES, IV_BENCH_LOOPS, IV_BENCH_NESTEDLOOPS, IV_BENCH_FUNCCALLS, IV_BENCH_RETS, IV_BENCH_DEFERS, IV_BENCH_PANICS, IV_BENCH_RECOVERS, IV_BENCH_CC,
        IV_CODE_IFS, IV_CODE_SWITCHES, IV_CODE_SWITCHCASES, IV_CODE_LOOPS, IV_CODE_NESTEDLOOPS, IV_CODE_FUNCCALLS, IV_CODE_RETS, IV_CODE_DEFERS, IV_CODE_PANICS, IV_CODE_RECOVERS, IV_CODE_CC,
    ],
)

IV_GROUP_PL_DATA = (
    'iv_group_pl_data',
    [
        IV_BENCH_VARS, IV_BENCH_PTRS, IV_BENCH_SLICES, IV_BENCH_MAPS,
        IV_CODE_VARS, IV_CODE_PTRS, IV_CODE_SLICES, IV_CODE_MAPS,
    ],
)

IV_GROUP_PL_CONC = (
    'iv_group_pl_conc',
    [
        IV_BENCH_GOS, IV_BENCH_CHANNELS, IV_BENCH_CHSENDS, IV_BENCH_CHRECS, IV_BENCH_CHCLOSES, IV_BENCH_CHRANGES, IV_BENCH_SELECTS, IV_BENCH_SELECTCASES,
        IV_CODE_GOS, IV_CODE_CHANNELS, IV_CODE_CHSENDS, IV_CODE_CHRECS, IV_CODE_CHCLOSES, IV_CODE_CHRANGES, IV_CODE_SELECTS, IV_CODE_SELECTCASES,
    ],
)

IV_GROUP_LIB = (
    'iv_group_lib',
    [
        IV_BENCH_STDLIB_BUFIO, IV_BENCH_STDLIB_BYTES, IV_BENCH_STDLIB_CRYPTO, IV_BENCH_STDLIB_DATABASE_SQL, IV_BENCH_STDLIB_ENCODING, IV_BENCH_STDLIB_ENCODING_BINARY, IV_BENCH_STDLIB_ENCODING_CSV, IV_BENCH_STDLIB_ENCODING_JSON,
        IV_BENCH_STDLIB_ENCODING_XML, IV_BENCH_STDLIB_IO, IV_BENCH_STDLIB_IO_IOUTIL, IV_BENCH_STDLIB_MATH, IV_BENCH_STDLIB_MATH_RAND, IV_BENCH_STDLIB_MIME, IV_BENCH_STDLIB_NET, IV_BENCH_STDLIB_NET_HTTP, IV_BENCH_STDLIB_NET_HTTP_HTTPTEST,
        IV_BENCH_STDLIB_NET_HTTP_HTTPTRACE, IV_BENCH_STDLIB_NET_HTTP_HTTPUTIL, IV_BENCH_STDLIB_NET_RPC, IV_BENCH_STDLIB_NET_RPC_JSONRPC, IV_BENCH_STDLIB_NET_SMTP, IV_BENCH_STDLIB_NET_TEXTPROTO, IV_BENCH_STDLIB_OS,
        IV_BENCH_STDLIB_OS_EXEC, IV_BENCH_STDLIB_OS_SIGNAL, IV_BENCH_STDLIB_SORT, IV_BENCH_STDLIB_STRCONV, IV_BENCH_STDLIB_SYNC, IV_BENCH_STDLIB_SYNC_ATOMIC, IV_BENCH_STDLIB_SYSCALL,
        IV_CODE_STDLIB_BUFIO, IV_CODE_STDLIB_BYTES, IV_CODE_STDLIB_CRYPTO, IV_CODE_STDLIB_DATABASE_SQL, IV_CODE_STDLIB_ENCODING, IV_CODE_STDLIB_ENCODING_BINARY, IV_CODE_STDLIB_ENCODING_CSV, IV_CODE_STDLIB_ENCODING_JSON,
        IV_CODE_STDLIB_ENCODING_XML, IV_CODE_STDLIB_IO, IV_CODE_STDLIB_IO_IOUTIL, IV_CODE_STDLIB_MATH, IV_CODE_STDLIB_MATH_RAND, IV_CODE_STDLIB_MIME, IV_CODE_STDLIB_NET, IV_CODE_STDLIB_NET_HTTP, IV_CODE_STDLIB_NET_HTTP_HTTPTEST,
        IV_CODE_STDLIB_NET_HTTP_HTTPTRACE, IV_CODE_STDLIB_NET_HTTP_HTTPUTIL, IV_CODE_STDLIB_NET_RPC, IV_CODE_STDLIB_NET_RPC_JSONRPC, IV_CODE_STDLIB_NET_SMTP, IV_CODE_STDLIB_NET_TEXTPROTO, IV_CODE_STDLIB_OS,
        IV_CODE_STDLIB_OS_EXEC, IV_CODE_STDLIB_OS_SIGNAL, IV_CODE_STDLIB_SORT, IV_CODE_STDLIB_STRCONV, IV_CODE_STDLIB_SYNC, IV_CODE_STDLIB_SYNC_ATOMIC, IV_CODE_STDLIB_SYSCALL,
    ],
)

IV_GROUP_IO = (
    'iv_group_io',
    [
        IV_BENCH_STDLIB_BUFIO, IV_BENCH_STDLIB_DATABASE_SQL, IV_BENCH_STDLIB_IO, IV_BENCH_STDLIB_IO_IOUTIL, IV_BENCH_STDLIB_MIME, IV_BENCH_STDLIB_NET, IV_BENCH_STDLIB_NET_HTTP, IV_BENCH_STDLIB_NET_HTTP_HTTPTEST, IV_BENCH_STDLIB_NET_HTTP_HTTPTRACE, IV_BENCH_STDLIB_NET_HTTP_HTTPUTIL, IV_BENCH_STDLIB_NET_RPC, IV_BENCH_STDLIB_NET_RPC_JSONRPC, IV_BENCH_STDLIB_NET_SMTP, IV_BENCH_STDLIB_NET_TEXTPROTO,
        IV_CODE_STDLIB_BUFIO, IV_CODE_STDLIB_DATABASE_SQL, IV_CODE_STDLIB_IO, IV_CODE_STDLIB_IO_IOUTIL, IV_CODE_STDLIB_MIME, IV_CODE_STDLIB_NET, IV_CODE_STDLIB_NET_HTTP, IV_CODE_STDLIB_NET_HTTP_HTTPTEST, IV_CODE_STDLIB_NET_HTTP_HTTPTRACE, IV_CODE_STDLIB_NET_HTTP_HTTPUTIL, IV_CODE_STDLIB_NET_RPC, IV_CODE_STDLIB_NET_RPC_JSONRPC, IV_CODE_STDLIB_NET_SMTP, IV_CODE_STDLIB_NET_TEXTPROTO,
    ],
)

IV_GROUP_LIB_CONC = (
    'iv_group_lib_conc',
    [
        IV_BENCH_STDLIB_SYNC, IV_BENCH_STDLIB_SYNC_ATOMIC,
        IV_CODE_STDLIB_SYNC, IV_CODE_STDLIB_SYNC_ATOMIC,
    ],
)

IV_GROUP_MATH = (
    'iv_group_math',
    [
        IV_BENCH_STDLIB_MATH, IV_BENCH_STDLIB_MATH_RAND,
        IV_CODE_STDLIB_MATH, IV_CODE_STDLIB_MATH_RAND,
    ],
)

IV_GROUP_STR = (
    'iv_group_str',
    [
        IV_BENCH_STDLIB_BYTES, IV_BENCH_STDLIB_CRYPTO, IV_BENCH_STDLIB_ENCODING, IV_BENCH_STDLIB_ENCODING_BINARY, IV_BENCH_STDLIB_ENCODING_CSV, IV_BENCH_STDLIB_ENCODING_JSON, IV_BENCH_STDLIB_ENCODING_XML, IV_BENCH_STDLIB_MIME, IV_BENCH_STDLIB_SORT, IV_BENCH_STDLIB_STRCONV,
        IV_CODE_STDLIB_BYTES, IV_CODE_STDLIB_CRYPTO, IV_CODE_STDLIB_ENCODING, IV_CODE_STDLIB_ENCODING_BINARY, IV_CODE_STDLIB_ENCODING_CSV, IV_CODE_STDLIB_ENCODING_JSON, IV_CODE_STDLIB_ENCODING_XML, IV_CODE_STDLIB_MIME, IV_CODE_STDLIB_SORT, IV_CODE_STDLIB_STRCONV,
    ],
)

IV_GROUP_OS = (
    'iv_group_os',
    [
        IV_BENCH_STDLIB_OS, IV_BENCH_STDLIB_OS_EXEC, IV_BENCH_STDLIB_OS_SIGNAL, IV_BENCH_STDLIB_SYSCALL,
        IV_CODE_STDLIB_OS, IV_CODE_STDLIB_OS_EXEC, IV_CODE_STDLIB_OS_SIGNAL, IV_CODE_STDLIB_SYSCALL,
    ],
)

IV_GROUP_NONE = (
    'iv_group_none',
    [],
)

# List of lists of features that form groups.
IV_GROUPS = [
    IV_GROUP_NONE,
    IV_GROUP_BENCH,
    IV_GROUP_CODE,
    IV_GROUP_META,
    IV_GROUP_PL,
    IV_GROUP_PL_CF,
    IV_GROUP_PL_DATA,
    IV_GROUP_PL_CONC,
    IV_GROUP_LIB,
    IV_GROUP_IO,
    IV_GROUP_LIB_CONC,
    IV_GROUP_MATH,
    IV_GROUP_STR,
    IV_GROUP_OS,
]