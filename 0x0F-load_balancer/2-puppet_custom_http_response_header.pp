class nginx_custom_header {

  package { 'nginx':
    ensure => installed,
  }

  $header_line = "add_header X-Served-By ${::hostname};"

  file_line { 'nginx-header':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => $header_line,
    match  => '^add_header X-Served-By',
    require => Package['nginx'],
    notify => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File_line['nginx-header'],
  }
}

include nginx_custom_header

