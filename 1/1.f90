program one
  implicit none
  character(len=10) :: filename, line, dist

  character(len=1) :: dir
  integer :: num_lines, i, loc, zero_count, dist1, num_rots
  logical :: crossed_zero
  filename="input"
  call read_input_size(filename, num_lines)

  open(20, file=filename)

  ! Starts at 50
  zero_count = 0
  loc = 50
  crossed_zero = .false.
  do i = 1, num_lines
    read(20,*) line
    line = trim(adjustl(line))
    dir = line(1:1)
    dist = line(2:len(line))
    read(dist, *) dist1
    num_rots = dist1/100 
    zero_count = zero_count + num_rots
    dist1 = mod(dist1,100)
    if(dir == "L") then
      if (loc - dist1 < 0) then
        if(loc /= 0) then
          write(*,*) "Crossed zero"
          zero_count = zero_count + 1 
        end if
        loc = 100 + (loc - dist1)
        
      else
        loc = loc - dist1
      end if
    end if
    if(dir == "R") then
      if (loc + dist1 > 99) then
        if(loc /= 0 .and. (((loc + dist1) - 100)) /= 0) then
          write(*,*) "Crossed zero"
          zero_count = zero_count + 1 
        end if
        loc = (loc + dist1) - 100
        
      else
        loc = loc + dist1
      end if
    end if
    if(loc == 0) zero_count = zero_count + 1
    write(*,*) loc
  end do
  write(*,*) "Part 1 answer = ", zero_count


contains
subroutine read_input_size(file, num_lines)
  implicit none

  character(*), intent(in) :: file
  integer, intent(out)     :: num_lines

  integer :: i, istat
  character(20) :: trash

  num_lines = 0
  open(20, file=file)
  do 
    read(20,*, iostat=istat)  trash
    if(istat /= 0) exit
    num_lines = num_lines + 1
  end do
  close(20)

end subroutine
end program
