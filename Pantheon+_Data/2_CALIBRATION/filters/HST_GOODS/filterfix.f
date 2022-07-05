      PROGRAM FILTERFIX
C-------------------------
C Fix up HST filter discriptions
C Read in wavelength and throughput
C Interpolate between the bins to give even bin sizes
C--------------------------
C
      IMPLICIT NONE
C
      INTEGER NFILT,IFILT
      PARAMETER (NFILT=8)
c
      CHARACTER*20 FNAME(NFILT),FNAMEI(NFILT)
      DATA FNAME /
     & 'F110W_NIC2.dat',
     & 'F160W_NIC2.dat',
     & 'F606W_ACS.dat',
     & 'F675W_WFPC2.dat',
     & 'F775W_ACS.dat',
     & 'F814W_WFPC2.dat',
     & 'F850LP_ACS.dat',
     & 'F850lp_WFPC2.dat'/

      INTEGER NLAM,ILAM,JLAM,KLAM,NLAMI
      PARAMETER (NLAM=15000)

      REAL LAM(NLAM),THROUG(NLAM)
      REAL LAMX,LAMN,LAMS
C
      REAL LAMI(NLAM),THROUGI(NLAM)
C
      DO IFILT = 1,NFILT
        OPEN (UNIT=30,FILE=FNAME(IFILT),FORM='FORMATTED')
        ILAM = 0
 100    CONTINUE
          ILAM = ILAM + 1
          READ (30,'(11X,F9.3,9X,F12.10)',END=101) LAM(ILAM),
     &                                             THROUG(ILAM)
        GOTO 100
 101    CONTINUE
        CLOSE(30)

C OK fix up

        JLAM = ILAM -1
        LAMN = LAM(1)
        LAMX = LAM(JLAM)
        LAMS = 5.0
        NLAMI = NINT((LAMX-LAMN)/LAMS) + 1
        DO ILAM = 1,NLAMI
          LAMI(ILAM) = LAMN + FLOAT(ILAM-1)*LAMS
          DO KLAM = 1,JLAM-1
            THROUGI(ILAM) = 0.0
            IF (LAMI(ILAM).GE.LAM(KLAM).AND.
     &          LAMI(ILAM).LT.LAM(KLAM+1)) THEN
              THROUGI(ILAM) = THROUG(KLAM) + 
     &                        ((LAMI(ILAM)-LAM(KLAM))/
     &                         (LAM(KLAM+1)-LAM(KLAM)))*
     &                        (THROUG(KLAM+1) - THROUG(KLAM))
              GOTO 200
            ENDIF
          ENDDO
 200      CONTINUE
        ENDDO

C Write out the fixed up

        FNAMEI(IFILT) = 'new'//FNAME(IFILT)        
        OPEN (UNIT=30,FILE=FNAMEI(IFILT),FORM='FORMATTED')
        DO ILAM = 1,NLAMI
          WRITE(30,'(5X,F8.2,5X,F8.6)') LAMI(ILAM),THROUGI(ILAM)
        ENDDO
        CLOSE(30)

      ENDDO

      END
