#!/usr/bin/pup
#installs flask (v2.1.0) from pip3

package {'python3-pip':
  ensure => present,
}

exec {'install flask':
  command     => 'pip3 install "flask==2.1.0"',
  unless      => 'pip3 show flask | grep "Version: 2.1.0"',
  path        => ['/usr/local/bin/', '/usr/bin/', '/bin'],
  user        => root,
  environment => ['HOME=/root'],
}

