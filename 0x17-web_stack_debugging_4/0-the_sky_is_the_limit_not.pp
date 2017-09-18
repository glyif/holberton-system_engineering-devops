#changes ulimit of nginx
include nginx
#changing nginx to not fail
class nginx {

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  file { '/etc/default/nginx':
    notify  => Service['nginx'],
    path    => '/etc/default/nginx',
    replace => true,
    content => 'ULIMIT="-u 4096"'
    }
}
