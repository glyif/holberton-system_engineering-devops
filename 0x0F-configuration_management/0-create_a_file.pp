# creating a file in /tmp called holberton, setting permissions and content

file { 'holberton':
  ensure  => file,
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}


