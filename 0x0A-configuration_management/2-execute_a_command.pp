#kills killmenow file

exec {'pkill-killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
