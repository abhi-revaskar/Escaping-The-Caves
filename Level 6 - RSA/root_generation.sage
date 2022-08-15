def decrypt_RSA(pad, max_root_len):
    global e, C, ZmodN #accessing global variables
    
    binary_pad = ''.join(['{0:08b}'.format(ord(x)) for x in pad])  #getting binary form of padding string 
    beta = 1
    eps = beta / 7
    flag = 0
    for root_len in range(0, max_root_len+1, 4): #iterating over all root lengths in multiples of 4
        P.<M> = PolynomialRing(ZmodN)
        pol = ((int(binary_pad , 2)*(2^root_len) + M)^e - C)
        dd = pol.degree()                   
        m = ceil(beta**2 / (dd * (eps))) 
        t = floor(dd * m * ((1/beta) - 1))    
        X = ceil(N**((beta**2/dd) - eps))  

        roots = coppersmith(pol, N, beta, m, t, X) #getting roots from coppersmith function

        if roots:
            print("Root found :", ' {0:b}'.format(roots[0]))
            flag = 1
            break
    if flag==0:
        print('Solution not found')

def coppersmith(pol, modulus, beta, mm, tt, XX):
    
    dd = pol.degree()
    nn = dd * mm + tt

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)

    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
    
    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots

e = 5
C = 34171865506568761235366341493790588282544840980265985400868758217892290366974519206338316594138947784237705432193781201437528572525674984876315116214158247120512293095872879010604762678625568544043246569469048652272836435130693197728856983127258786909134464110413886711222381976246871928091620326451745412077
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093

ZmodN = Zmod(N);

if __name__ == "__main__":
    decrypt_RSA("DECODERS: This door has RSA encryption with exponent 5 and the password is ", 200)