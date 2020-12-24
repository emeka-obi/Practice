def merge_point(head1,head2):
    marker1 = head1
    marker2 = head2
    while(marker1 != marker2):
        if marker1.next == None:
            marker1 = head2
        else:
            marker1 = marker1.next
        if marker2.next == None:
            marker2 =  head1
        else:
            marker2 = marker2.next
    return marker1.data