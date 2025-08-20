function Home() {
  return (
    <>
    <div style={{
        width: "100vw",
        display:"flex",
        justifyContent: "center",
        flexDirection: "column"
    }}>
        <div style={{
            width: "80vw",
            display: 'flex',
            flexDirection: "column",
            alignItems: "center"
        }}>
            <h2> Seja bem vindo!!!</h2>
            <p>Expresse aqui seus pensamentos e opiniões</p>
        </div>
        <div style={{
            width: "80vw",
            display: 'flex',
            flexDirection: "column",
            alignItems: "center"
        }}>
            <img src="https://sep-bucket-prod.s3.amazonaws.com/wp-content/uploads/2025/08/14082025_cg_palmeiras_destaque_5508_46.jpg"
            alt="Imagem palmeiras e universitario" 
            width="400px" 
            />
        </div>
    </div>
    </>
  )
}

export default Home