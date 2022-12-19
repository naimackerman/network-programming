<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>tes</title>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@2.43.1/dist/full.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body>
    <div class="container min-w-max min-h-screen">
        <div class="flex flex-col items-center justify-center h-min w-screen pt-3">
            <div class="flex flex-col items-center justify-center space-y-4">
                <div class="text-4xl font-bold">Simple Encrypt Decrypt Web</div>
                <div class="text-xl">DES-ECB</div>
                <div class="text-md">NAIM, OPI, JAGAD</div>
            </div>
        </div>
        <div class="m-5 mt-16 grid grid-cols-5 gap-4 w-auto">
            <div class="col-span-2">
                <textarea class="textarea textarea-bordered" placeholder="Plaintext" style="width: -webkit-fill-available;"></textarea>
            </div>
            <div class="col-span-1">
                <textarea class="textarea textarea-bordered" placeholder="Secret Key" style="width: -webkit-fill-available;"></textarea>
            </div>
            <div class="col-span-2">
                <textarea class="textarea textarea-bordered" placeholder="Result" style="width: -webkit-fill-available;"></textarea>
            </div>
        </div>
        <div class="w-auto text-center">
            <button class="btn btn-primary">Encrypt</button>
            <button class="btn btn-primary">Decrypt</button>
        </div>
        <div class="absolute bottom-0 bg-neutral text-center text-neutral-content p-5">
            Disusun Oleh: Naim, Opi, Jagad
        </div>
    </div>
</body>

</html>