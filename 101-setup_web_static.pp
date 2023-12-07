# Configuring my Ubuntu for deployment

exec { 'apt_update':
  command => 'apt-get -y update',
}

package { 'nginx':
  ensure => installed,
}

file { ['/data/web_static/releases/test/', '/data/web_static/shared/']:
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Testing my server',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file_line { 'nginx_location_block':
  path   => '/etc/nginx/sites-available/default',
  line   => '        location /hbnb_static/ {',
  after  => '        location / {',
  before => '        location ~ \\.php$ {',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('path/to/nginx_config.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
