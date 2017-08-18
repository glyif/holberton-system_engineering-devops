exec { 'kill_process':
  command => 'pkill -f killmenow',
  returns => '0',
  path    => ['/usr/bin']
}
