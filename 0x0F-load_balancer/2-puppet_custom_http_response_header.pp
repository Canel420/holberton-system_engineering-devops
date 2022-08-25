# Install HTTP header on ubuntu server.
include stdlib

exec { "system-update":
    command => "/usr/bin/apt -y update"
}

package { "Nginx":
    ensure => "installed" 
}

file { 'Nginx config':
  ensure => present,
  path   => '/etc/nginx/nginx.conf',
  mode   => '0777'
}

file_line { 'add http header':
  path  => '/etc/nginx/nginx.conf',
  line  => "\tadd_header X-Served-By ${HOSTNAME};",
  after => 'http {',
}

exec { 'Restart web server':
    command => '/usr/bin/service nginx restart'
}
