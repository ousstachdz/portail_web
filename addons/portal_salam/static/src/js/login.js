class LoginIndex extends Component {
  setup() {
    this.state = useState({
      formData: {
        login: '',
        password: '',
      },
    })
    this.handleChange = this.handleChange.bind(this)
  }
  handleChange(event) {
    const { name, value } = event.target
    this.state.formData[name] = value
  }
  async handleLogin(e) {
    e.preventDefault()

    const { login, password } = this.state.formData

    if (!login || !password) {
      alert('Please enter both login and password.')
      return
    }

    try {
      const result = await fetch('/web/session/authenticate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          jsonrpc: '2.0',
          method: 'call',
          params: {
            db: 'odoo_essalam',
            login: login,
            password: password,
          },
        }),
      })

      const responseData = await result.json()
      console.log('Login response:', responseData)

      if (responseData.result && responseData.result.uid) {
        window.location = '/'
      } else {
        alert('Incorrect login or password.')
      }
    } catch (error) {
      console.error('Login failed:', error)
      alert('An error occurred while attempting to log in. Please try again.')
    }
  }
  static template = xml`
 <div class="d-flex flex-column align-items-center" dir='rtl'>
    <div class="col-12">

      <div class="bg-light p-3 rounded shadow-sm mb-4">
        <h5>تسجيل الدخول</h5>

        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="login">بريد إلكتروني</label>    
              <input type="email"
              class="form-control"
              id="login" 
              name="login" 
              t-att-value="state.formData.login"
              t-on-keyup="handleChange" 
              required="required"/>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="password">كلمة السر</label>
              <input type="password" 
              class="form-control"
              id="password" 
              t-att-value="state.formData.password"
              name="password" 
              t-on-keyup="handleChange" 
              required="required"
              />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
            </div>
          </div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <button type="button" t-on-click="handleLogin" class="btn btn-primary green-btn">
                    تسجيل الدخول
                </button>
            </div>
        </div>
      </div>
    </div>
  </div>
    `
}

document.getElementById('login_portail') &&
  mount(LoginIndex, document.getElementById('login_portail'))
