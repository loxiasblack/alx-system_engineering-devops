exec { "killmenow":
    command => "pkill -f killmenow || true",
    path => '/bin:/usr/bin:sbin:/usr/sbin',
}
