#!/usr/bin/pup
#installs flask (v2.1.0) from pip3

package {'python3-pip':
  ensure => present,
}

exec {'install flask':
  command => 'pip3 install flask',
  ensure  => '2.1.0'
  unless  => 'pip3 show flask',
  path    => ['/usr/local/bin/', '/usr/bin/', '/bin'],
  user    => 'root',
}

