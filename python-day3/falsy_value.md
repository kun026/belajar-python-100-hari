# Nilai Falsy dalam Python

Dalam Python, beberapa nilai dianggap "falsy" yang berarti bahwa mereka dievaluasi sebagai `False` ketika digunakan dalam konteks yang memerlukan evaluasi Boolean, seperti dalam pernyataan `if`. Berikut adalah nilai-nilai yang dianggap falsy di Python:

1. `None`
2. `False`
3. Angka nol dari tipe apapun:
   - `0` (integer)
   - `0.0` (float)
   - `0j` (complex number)
4. String kosong: `""`
5. List kosong: `[]`
6. Tuple kosong: `()`
7. Set kosong: `set()`
8. Dictionary kosong: `{}`
9. Object dari kelas yang mendefinisikan metode `__bool__()` atau `__len__()` yang mengembalikan `False` atau `0`

## Contoh Penggunaan

Berikut adalah contoh penggunaan nilai-nilai falsy dalam konteks `if`:

```python
if not None:
    print("None is falsy")

if not False:
    print("False is falsy")

if not 0:
    print("0 is falsy")

if not 0.0:
    print("0.0 is falsy")

if not "":
    print("Empty string is falsy")

if not []:
    print("Empty list is falsy")

if not ():
    print("Empty tuple is falsy")

if not set():
    print("Empty set is falsy")

if not {}:
    print("Empty dictionary is falsy")
