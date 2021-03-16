#============================================================================#
#============================ARCANE CALCULATOR===============================#
#============================================================================#

import hashlib
from cryptography.fernet import Fernet
import base64



# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

username_trial = "PRITCHARD"
bUsername_trial = b"PRITCHARD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

star_db_trial = {
  "Alpha Centauri": 4.38,
  "Barnard's Star": 5.95,
  "Luhman 16": 6.57,
  "WISE 0855-0714": 7.17,
  "Wolf 359": 7.78,
  "Lalande 21185": 8.29,
  "UV Ceti": 8.58,
  "Sirius": 8.59,
  "Ross 154": 9.69,
  "Yin Sector CL-Y d127": 9.86,
  "Duamta": 9.88,
  "Ross 248": 10.37,
  "WISE 1506+7027": 10.52,
  "Epsilon Eridani": 10.52,
  "Lacaille 9352": 10.69,
  "Ross 128": 10.94,
  "EZ Aquarii": 11.10,
  "61 Cygni": 11.37,
  "Procyon": 11.41,
  "Struve 2398": 11.64,
  "Groombridge 34": 11.73,
  "Epsilon Indi": 11.80,
  "SPF-LF 1": 11.82,
  "Tau Ceti": 11.94,
  "YZ Ceti": 12.07,
  "WISE 0350-5658": 12.09,
  "Luyten's Star": 12.39,
  "Teegarden's Star": 12.43,
  "Kapteyn's Star": 12.76,
  "Talta": 12.83,
  "Lacaille 8760": 12.88
}


def intro_trial():
    print("\n===============================================\n\
Welcome to the Arcane Calculator, " + username_trial + "!\n")    
    print("This is the trial version of Arcane Calculator.")
    print("The full version may be purchased in person near\n\
the galactic center of the Milky Way galaxy. \n\
Available while supplies last!\n\
=====================================================\n\n")


def menu_trial():
    print("___Arcane Calculator___\n\n\
Menu:\n\
(a) Estimate Astral Projection Mana Burn\n\
(b) [LOCKED] Estimate Astral Slingshot Approach Vector\n\
(c) Enter License Key\n\
(d) Exit Arcane Calculator")

    choice = input("What would you like to do, "+ username_trial +" (a/b/c/d)? ")
    
    if not validate_choice(choice):
        print("\n\nInvalid choice!\n\n")
        return
    
    if choice == "a":
        estimate_burn()
    elif choice == "b":
        locked_estimate_vector()
    elif choice == "c":
        enter_license()
    elif choice == "d":
        global arcane_loop_trial
        arcane_loop_trial = False
        print("Bye!")
    else:
        print("That choice is not valid. Please enter a single, valid \
lowercase letter choice (a/b/c/d).")


def validate_choice(menu_choice):
    if menu_choice == "a" or \
       menu_choice == "b" or \
       menu_choice == "c" or \
       menu_choice == "d":
        return True
    else:
        return False


def estimate_burn():
  print("\n\nSOL is detected as your nearest star.")
  target_system = input("To which system do you want to travel? ")

  if target_system in star_db_trial:
      ly = star_db_trial[target_system]
      mana_cost_low = ly**2
      mana_cost_high = ly**3
      print("\n"+ target_system +" will cost between "+ str(mana_cost_low) \
+" and "+ str(mana_cost_high) +" stone(s) to project to\n\n")
  else:
      # TODO : could add option to list known stars
      print("\nStar not found.\n\n")


def locked_estimate_vector():
    print("\n\nYou must buy the full version of this software to use this \
feature!\n\n")


def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")


def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return True


def decrypt_full_version(key_str):

    key_base64 = base64.b64encode(key_str.encode())
    f = Fernet(key_base64)

    try:
        with open("keygenme.py", "w") as fout:
          global full_version
          global full_version_code
          full_version_code = f.decrypt(full_version)
          fout.write(full_version_code.decode())
          global arcane_loop_trial
          arcane_loop_trial = False
          global jump_into_full
          jump_into_full = True
          print("\nFull version written to 'keygenme.py'.\n\n"+ \
                 "Exiting trial version...")
    except FileExistsError:
    	sys.stderr.write("Full version of keygenme NOT written to disk, "+ \
	                  "ERROR: 'keygenme.py' file already exists.\n\n"+ \
			  "ADVICE: If this existing file is not valid, "+ \
			  "you may try deleting it and entering the "+ \
			  "license key again. Good luck")

def ui_flow():
    intro_trial()
    while arcane_loop_trial:
        menu_trial()



# Encrypted blob of full version
full_version = \
b"""
gAAAAABgT_nvf4P0-CFwlBsPrO8lFGYdOMPOsW49NMCVP4OQm4TqUiwWH6wolWNozf6wSudqEnLxlV6_tpyRrEDHQjBf05wp3N8eVOlkGtbYvQ1j3rJp5A-u68f04WfV-Tbx87qMXkicUYywezrlklzxOtOGeqatlaT9uQXVHu9FyZbYmcKGrpQ5gnGc-u278DYd2vmYgo8Y4gsf0DsRy3R3OhpI9oAYBtoThP6A2kwvggWAYUTNv6VQ3mcpwgwGqJP6tro8BHkGJVW2xQMiptJfXWdANIAQOoL9Xse3spqlSmnaZzTZ2nGpWtzPsGXXbBo2YRV1tRm4HNeS4VpSnHPVd5nNBe7hTckqs_ye1WkG58z1ldo7fvLDRudVMrjBYSsQHd64XMaq5KFZeKWtm0F6r5DYK5d5UFhZzZi8F7PIQZ481lgTb4QxBu0HvsMcjk9r10aeKHzMxYDEpq8o9xZXlBhYMB9N6919y2Deuk2-VICbc2RX5NMzBjIfqnwJvWG7w8ystaiN-BxATHHcvSuV6_3tsGqEbJi7wILo2sMBiAa_a3pLDnIovXhG3dqbxR0Ay9fQFSJvcUqqbyXcK5MPs52_iZWJ2wD27ac6EQP911pHwaE6N_7p3u8zHOzMk4LDSZJhADeotihRJYXuAw3laDfOVWo1H2JoLGfuU6--4PcJAqQz1ZRTXWEkP6hcd2UtXKZVF8kzGTRyl5KSbMoU2ZJGSXrVZMpjdFE5WON_ZBa-TAdw537NZvr-bVINw8oPmb39n3VYRQFB_bkuUHcgHqVaexTIrAVL10jJdyIQtVRaZdxWkmdhNNWgkhSXozz9oatq_PYVlb_6aiWD8co4l019-H8dhrZHqMUR06JryR3aDcV85eFKSQKWfs5gS67vJYfPj3V7SJVUtS30jGEjZQO8mmBnncBOX927pBxZKtwn111m9Ryr-Lwack7UWQj4JFIDgHwXghN7ScGQDc3BNQImfutCuVFf9MVOCb7QZru0icd7o3eEztFDPHOZQIKSDBq7zfmZBgppEFZjouAUO4d97hkcnSGf6nRM2oqhwt_9N5h_e3SntRNJGoPfHrjsWutGZO-2kaw6kFIVsL0QBdMDS2V8oFFCpMiNoWS1OvrILvzT-UGtQKtfmC0H-zR1CL3PQGfPbcgW08EmkuSPrZk-bKTucvz6r_9PxQPMznyhpm_5f1MhYt_eKkwpkRS9zChuNtb3vP2Qp3M5CUdWpxA3dNmrarihWka94RCuUDftROcBIWpNUrWci-fkDCzeYHwFs_qH3DK85dKpmQVnmHrrRG2rH9Y1jW2jpqmEHiZKjc6tQa2kmRVR9vDvaygFjDAzGk7b2h7nLFHCKPvJnvkw-yvSIL8GVHVTWhe2PhK983qu2RQIlL3R-27Xzx_pz_0OehnosqeZkY19T1Jzri2BcL9HYB_qAdniXONU36zj9ZiUs_Ffpq4OgiVw2-bBLIDEtpN2xSj2P7-An_Xjtbgr0ukMdEUjFLV4yScjaqDBM7kM1rE2l4fFPY0pEMy3aasIAJRL9mDS04jLDCsZn_BxxIlOpnVBvHZld_rRyRWtbN3UESj6jl2pHIxzgvMg9E8Eyt8XT7bgRfimMDrocMahrGhE018t3xTNDtNHgnoaD2t4DyqQr1pr6TcMKRxNqqXy3dEYvKDVhBmzFc00YKkT6bp0ufwpzlknFnEEmHh6QAoxdM5uD_3QEm1X67gtwoOXFtY3TSGJ9CzfWsOeQ_BjxyWJkm4W6b3SbnlJ68hsTXUk6Cc3uzoczgwCeyb6uSw5O9cHT-s5KTpHlnISkB0SYs4pZMHcQ-gq3URPYTeGP11KLfWCMuznCosYc3R7jriReKKOjFD2CU2Fc-i_CmlkRJ4tqDhKZFx3UhBCUQY4JVAOS8RQTb1T9qW-mNe8JcDEpPirqNMI_wL3EFWKyd8jQGM38mRjkq2p2jf9HRNVvmpyFNWxiOP8jsG3RvtiGS3Nv58D417EgRUCG_FEQiHRKmxjuUIAmpGEioln2Yf3sGYoBfvhwlZinTdpiVoUwjRAZdRXMvoYhRQnIT7ykQlTax64DS4RxHeFjaO6FyWMR3rDkRQSvMsUTzmFGVST564CfvSUHKPIz91SNcgbQoR5Y3-4GS50qX87sBu8ow-Z6zquzMDavkpBJzxrB1NX0Tez1SREt4ViK3Hi5Jvr1r8uKTDgjH62v5HBRZlqlMOQBXPBKAAMPUOqqsqKbil6NOiOADezhcYfc4Vy3N11AfL3mx2AIHpLfdtYcUzsuImPpAu6V75_zD5GdzGdb-N3uYPJrkKmQOoK61HsJQjVjgluoNHavR13fJ0FQWYJpEyn4P1Tuhkv4pgtYMtiXHwC6804DdsTMdgFrTR3K0E-xwDq0E68pkcebW7hZAuXE3Qhxviyb6BHx5E_recW3q2Od7_J_CSiECgf_0ykLuKZM4aQBLp7UM9aafK109Z6rwGDdsJ3_C5u0RIZ6gh5d_lRtWroUzsTryuM-XqRe_xuIbLzYBeAqSjovbKFIeev3vJ3KdNRVO65kBJUaOIGn7uv6Qv2am4Hfo-wu86J2wKyMaAUsL0TEyKKInh03rg1IQY84xdAEeqVSStn3fU5GdnxYrt-ByhvTNAoXhGGKPjzhzLdvgBB07Or9OtjvjyDByD8KFpolp1_TiMnDW6Rp66HQlqFgqgrEA0Ix3-nkU_R2yC8xR2QEvD2A9JxKKwc03NtwmlKi9NlslYKLS0g7lu3CombAx7AqAMIF__kM8czRVV9Np-IvDp2CZEArvryF_Oo0CKszZy2ngXZbSD1bobYDa6168yUNGyaL-nbDiB28QL1wiDjLL6vF-dYU2Q9-cVuE11bSZOzbARbr-oaMHC6QACNbs6vpF6Tq9tOJdEbUfAwXt-BEk3KlAW7mcYgpFvADD6ZdefN99lCoAJSljgy243CMEfw8WGfNUMh8uHKsmcHie089aiJLlzEs5o0MacV43ttbgBQ0rMD7e5KHf56dqDO0k15E9UsYsiniGbs8sNPRL-SQzpZqWBd4z2gEXc9_l7xMv_GpXBz4Dj7OJKu7TzD5Vvmd54wqWcMPo7MMIpMY6xyUIZgK9IvUc_dRkV9ze3FfaJi656TBo4Fw1MgURqyRx8kCUsMCqGJgftryPMA0iA0ha3_9dEIZKyJwt51I1JltO6GUQTMYa9nvmcbFyxH3XIgjjT2T8X1vrPZqYDJ0BMIV1OlweD_V69NjykDxa879r-SvSByONyeTrqe_yDfBKxjVJPPmSy9U9uIN8mjuPOjbHnnG_vjsACp22slbyv5Qc75znhhwQe7KuxCIuf3WfZi_WDMXxWKXaaM-Q4o8qM5B3Ak2lC1VyalFvUkLA-aUTrj1RgQ6FziAA14l9cQQu4hJJ0mOBdmcAd_cpbCkD2ADlA-IxYcIXflwDWf-WUO8b-QzuHie3g0V6dzlCN9B56w6XlwhkeTS4OQdmtIBVZvhqBXJpXzmHBLlHwirF4COCWSn5w_Q7D9z1kq0RjMyzqrq36UTVGjKfWxMKVvnd1RQkn3PsddwJG62Dfaty3td43RyTUvsGwrTglZWe7v6229eYxDXwmgbtJ_eWSjdcyr9i38diyOLbDzs6xvdLL4bjR5WqB4YBcNFlXMvnyJxt4hiyDvZriJpmtsa7O58-ReW4KkbDo1RjrL20GeFfiQELW_V-11gvPoyLIigmTt4oluCleUDLuZ0gkhRLY9ve9f8kmQDsMLWSM2S-0xq4Q3QQZrOAHYEme3o5iROA2EU5lYwQGXXJIiVsIYzQWC2ULrmqJ67ceCwUgPzdCT8qnnhTETGwGDxFlLbJRiiqpNQ3WeGgEHFSN2bLQypC5CZwowIg==
"""



# Enter main loop
ui_flow()

if jump_into_full:
    exec(full_version_code)
